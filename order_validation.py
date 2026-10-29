# -*- coding: utf-8 -*-
"""Validation for website orders. Prices come from pricing.py only — never from the browser."""
import re

from pricing import calculate_cart, BOTTLES_PER_ITEM
from texts import LANGS

PHONE_RE = re.compile(r"^\+?[0-9][0-9 ()\-]{5,18}$")
CONTACT_METHODS = {"", "telegram", "whatsapp", "instagram"}
MAX_QTY_PER_LINE = 20
MAX_BOTTLES = 40


class OrderError(ValueError):
    pass


def _clean(value, lo, hi, field):
    s = " ".join(str(value or "").split())  # collapse whitespace/newlines
    if not lo <= len(s) <= hi:
        raise OrderError(f"bad {field}")
    return s


def validate_order(payload: dict) -> dict:
    if not isinstance(payload, dict):
        raise OrderError("bad payload")

    raw_items = payload.get("items")
    if not isinstance(raw_items, list) or not 1 <= len(raw_items) <= 10:
        raise OrderError("bad items")
    merged: dict[str, int] = {}
    for it in raw_items:
        if not isinstance(it, dict):
            raise OrderError("bad items")
        pid, qty = it.get("id"), it.get("qty")
        if pid not in BOTTLES_PER_ITEM or isinstance(qty, bool) or not isinstance(qty, int):
            raise OrderError("bad items")
        if not 1 <= qty <= MAX_QTY_PER_LINE:
            raise OrderError("bad quantity")
        merged[pid] = merged.get(pid, 0) + qty
    items = [{"id": k, "qty": v} for k, v in merged.items()]
    totals = calculate_cart(items)
    if not 1 <= totals["bottles"] <= MAX_BOTTLES:
        raise OrderError("bad quantity")

    name = _clean(payload.get("name"), 2, 80, "name")
    city = _clean(payload.get("city"), 2, 60, "city")
    address = _clean(payload.get("address"), 5, 200, "address")
    phone = str(payload.get("phone", "")).strip()
    if not PHONE_RE.match(phone):
        raise OrderError("bad phone")

    method = str(payload.get("contact_method") or "").strip().lower()
    if method not in CONTACT_METHODS:
        raise OrderError("bad contact method")
    handle = " ".join(str(payload.get("contact_handle") or "").split())[:60]

    if payload.get("consent") is not True:
        raise OrderError("consent required")

    lang = payload.get("lang")
    return {
        "items": items,
        "name": name, "phone": phone, "city": city, "address": address,
        "contact_method": method, "contact_handle": handle,
        "lang": lang if lang in LANGS else "en",
        "totals": totals,
    }
