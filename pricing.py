# -*- coding: utf-8 -*-
"""Server-side pricing — the single source of truth. Mirrors public/assets/js/pricing.js.
Integer GEL only. The browser's numbers are never trusted."""

UNIT_PRICE = 80
DISCOUNT_PERCENT = 20
MIN_BOTTLES_FOR_DISCOUNT = 2
BOTTLES_PER_ITEM = {"mane": 1, "cord": 1, "dual": 2}


def calculate_cart(items):
    """items: list of {"id": "mane"|"cord"|"dual", "qty": int}. Returns bottles/subtotal/discount/total."""
    bottles = 0
    for it in items:
        per = BOTTLES_PER_ITEM.get(it["id"])
        qty = it["qty"]
        if per is None or not isinstance(qty, int) or isinstance(qty, bool) or qty < 0:
            raise ValueError("invalid cart item")
        bottles += per * qty
    subtotal = bottles * UNIT_PRICE
    discount = subtotal * DISCOUNT_PERCENT // 100 if bottles >= MIN_BOTTLES_FOR_DISCOUNT else 0
    return {"bottles": bottles, "subtotal": subtotal, "discount": discount, "total": subtotal - discount}
