/* Mind Root — UI. Prices and discount come ONLY from pricing.js; the server recomputes everything. */
(function () {
  'use strict';

  document.documentElement.classList.add('js-ready');

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var SITE = window.SITE, I18N = window.I18N, Pricing = window.Pricing;
  var LANG_KEY = 'mindroot_lang';
  var PHONE_RE = /^\+?[0-9][0-9 ()\-]{5,18}$/;
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  var MAX_QTY = (window.CartStore && window.CartStore.MAX) || 20;

  /* ---------- Google Analytics 4 (GA4) E-commerce Tracking ---------- */
  function initAnalytics() {
    var gaId = SITE && SITE.gaId ? String(SITE.gaId).trim() : '';
    if (!gaId || /^\[/.test(gaId)) return;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', gaId);
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(gaId);
    document.head.appendChild(s);
  }
  function trackEvent(eventName, params) {
    try {
      if (typeof window.gtag === 'function') {
        window.gtag('event', eventName, params || {});
      }
    } catch (e) { /* ignore analytics errors */ }
  }
  initAnalytics();

  function safeStorage() {
    try { var s = window.localStorage; s.setItem('__t', '1'); s.removeItem('__t'); return s; } catch (e) { return null; }
  }
  var store = safeStorage();
  var cart = window.CartStore.create(store);
  var lang = pickLang();
  var doneState = null;

  function pickLang() {
    try { var l = store && store.getItem(LANG_KEY); if (I18N.langs.indexOf(l) > -1) return l; } catch (e) { /* ignore */ }
    return 'en';
  }
  function t(k) {
    var d = I18N.dict[lang];
    if (d && d[k] !== undefined) return d[k];
    var e = I18N.dict.en[k];
    return e !== undefined ? e : k;
  }
  function gel(n) { return n + ' ₾'; }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; });
  }
  function pname(id) { return id === 'dual' ? t('dual_name') : SITE.products[id].name; }
  var DUAL_LIST = Pricing.calculateCart([{ id: 'dual', qty: 1 }]).subtotal;       // 160
  var DUAL_DEAL = Pricing.calculateCart([{ id: 'dual', qty: 1 }]).total;          // 128

  /* ---------- bottle component ---------- */
  function bottleHTML(id, eager) {
    var p = SITE.products[id];
    return '<div class="bottle__cap"></div><div class="bottle__neck"></div><div class="bottle__body"><div class="bottle__label">' +
      '<img src="' + p.label + '" alt="Mind Root ' + esc(p.name) + ' — ' + SITE.label.capsules + ' capsules" width="541" height="513" ' +
      (eager ? 'fetchpriority="high"' : 'loading="lazy"') + ' decoding="async"></div></div>';
  }
  function renderBottles(root) {
    $$('[data-bottle]', root).forEach(function (el) {
      if (el.firstChild) return;
      el.innerHTML = bottleHTML(el.getAttribute('data-bottle'), !!el.closest('.hero'));
    });
  }

  /* ---------- i18n ---------- */
  function applyI18n(root) {
    $$('[data-i18n]', root).forEach(function (el) { el.textContent = t(el.getAttribute('data-i18n')); });
    $$('[data-i18n-html]', root).forEach(function (el) { el.innerHTML = t(el.getAttribute('data-i18n-html')); });
    $$('[data-i18n-attr]', root).forEach(function (el) {
      el.getAttribute('data-i18n-attr').split(';').forEach(function (pair) {
        var kv = pair.split(':');
        if (kv.length === 2) el.setAttribute(kv[0].trim(), t(kv[1].trim()));
      });
    });
  }
  function fillPrices() {
    $$('[data-price]').forEach(function (el) {
      var k = el.getAttribute('data-price');
      el.textContent = gel(k === 'unit' ? Pricing.UNIT_PRICE : k === 'dualList' ? DUAL_LIST : DUAL_DEAL);
    });
  }
  function setLang(l) {
    lang = l;
    try { store && store.setItem(LANG_KEY, l); } catch (e) { /* ignore */ }
    document.documentElement.lang = l;
    document.title = t('meta_title');
    var md = $('meta[name="description"]'); if (md) md.setAttribute('content', t('meta_desc'));
    $$('.lang button').forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-lang') === l)); });
    applyI18n(document);
    fillPrices();
    renderSteps(); renderFaq(); renderDetails(); renderFooter(); renderCart(); renderConsent();
    if (doneState) renderDone();
    renderBottles(document);
    observeReveals();
  }

  /* ---------- reveal on scroll ---------- */
  var io = null;
  function observeReveals() {
    var els = $$('.reveal:not(.is-in)');
    if (!('IntersectionObserver' in window)) { els.forEach(function (e) { e.classList.add('is-in'); }); return; }
    io = io || new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { threshold: 0.08 });
    els.forEach(function (e) { io.observe(e); });
  }

  /* ---------- static sections rendered from the dictionary ---------- */
  function renderSteps() {
    $('#stepsRoot').innerHTML = t('steps').map(function (s) {
      return '<li class="reveal"><h3>' + esc(s.t) + '</h3><p>' + esc(s.d) + '</p></li>';
    }).join('');
  }
  function renderFaq() {
    $('#faqRoot').innerHTML = t('faq').map(function (f) {
      return '<details class="reveal"><summary>' + esc(f.q) + '</summary><p>' + esc(f.a) + '</p></details>';
    }).join('');
  }
  function renderFooter() {
    var c = SITE.contact;
    function item(value, url) {
      var ph = /^\[/.test(value);
      return '<li>' + (url && !ph ? '<a href="' + esc(url) + '"' + (/^https?:/.test(url) ? ' target="_blank" rel="noopener"' : '') + '>' + esc(value) + '</a>'
        : '<span class="' + (ph ? 'ph' : '') + '">' + esc(value) + '</span>') + '</li>';
    }
    $('#footContact').innerHTML =
      item(c.email, 'mailto:' + c.email) +
      item(c.phone, 'tel:' + c.phone.replace(/[^+\d]/g, '')) +
      item(c.instagramHandle, c.instagramUrl) +
      item(c.telegramHandle, c.telegramUrl) +
      '<li>' + esc(c.place) + '</li>';
  }

  /* ---------- product detail sections ---------- */
  function extractDl(pid) {
    var p = SITE.products[pid];
    return '<dl><dt>' + esc(p.name) + ' — ' + esc(t('d_extract')) + '</dt><dd>' + esc(p.name) + ' ' + esc(p.part.toLowerCase()) + ' extract ' + esc(p.ratio) +
      ' (<i>' + esc(p.latin) + '</i>)</dd><dt>' + esc(t('d_amount')) + '</dt><dd>' + esc(p.amount) + '</dd></dl>';
  }
  function docItem(label, url) {
    return '<li>' + esc(label) + ': ' + (url ? '<a class="ph" href="' + esc(url) + '" target="_blank" rel="noopener">' + esc(t('d_open')) + '</a>'
      : '<span class="ph">' + esc(t('d_request')) + '</span>') + '</li>';
  }
  function detailHTML(id) {
    var L = SITE.label, dual = id === 'dual';
    var inside = dual ? '<p>' + esc(t('dual_inside')) + '</p>' + extractDl('mane') + extractDl('cord') : extractDl(id);
    var other = '<dl><dt>' + esc(t('d_other')) + '</dt><dd>' + esc(L.otherIngredients) + '</dd></dl>';
    var docs = (dual ? docItem(SITE.products.mane.name + ' — ' + t('d_coa'), SITE.docs.coaMane) + docItem(SITE.products.cord.name + ' — ' + t('d_coa'), SITE.docs.coaCord)
      : docItem(t('d_coa'), id === 'mane' ? SITE.docs.coaMane : SITE.docs.coaCord)) + docItem(t('d_halal'), SITE.docs.halal) +
      '<li>' + esc(t('d_batch')) + ': <span class="ph">' + esc(L.batch) + '</span></li>';
    var visual = dual
      ? '<div class="bottle bottle--sm" data-bottle="mane" style="--bw:116px"></div><div class="bottle bottle--sm" data-bottle="cord" style="--bw:116px"></div>'
      : '<div class="bottle bottle--lg" data-bottle="' + id + '"></div>';
    var price = dual
      ? '<div class="price"><s>' + gel(DUAL_LIST) + '</s><strong>' + gel(DUAL_DEAL) + '</strong></div>'
      : '<div class="price"><strong>' + gel(Pricing.UNIT_PRICE) + '</strong><small>' + esc(t('per_bottle')) + '</small></div>';
    return '<article class="detail reveal" id="product-' + id + '" aria-labelledby="h-' + id + '">' +
      '<div class="detail__visual">' + visual + '</div><div class="detail__body">' +
      '<h3 id="h-' + id + '">' + esc(pname(id)) + '</h3><p class="lead">' + esc(t(id + '_lead')) + '</p>' +
      '<div class="facts">' +
        '<div><h4>' + esc(t('d_inside')) + '</h4>' + inside + other + '</div>' +
        '<div><h4>' + esc(t('d_serving')) + '</h4><dl><dt>' + esc(t('d_size')) + '</dt><dd>' + esc(L.servingSize) + '</dd>' +
          '<dt>' + esc(t('d_capsules')) + '</dt><dd>' + L.capsules + (dual ? ' × 2' : '') + '</dd>' +
          '<dt>' + esc(t('d_servings')) + '</dt><dd>' + L.servings + (dual ? ' × 2' : '') + '</dd>' +
          '<dt>' + esc(t('d_use')) + '</dt><dd>' + esc(L.suggestedUse) + '</dd></dl></div>' +
        '<div><h4>' + esc(t('d_docs')) + '</h4><ul>' + docs + '</ul></div>' +
        '<div><h4>' + esc(t('d_storage')) + '</h4><p>' + esc(L.storage) + '</p><p class="note">' + esc(L.origin) + '</p></div>' +
      '</div>' +
      '<div class="mini"><details><summary>' + esc(t('q_med')) + '</summary><p>' + esc(t('a_med')) + '</p></details>' +
      '<details><summary>' + esc(t('q_doc')) + '</summary><p>' + esc(t('a_doc')) + '</p></details></div>' +
      '<div class="detail__cta">' + price + stepperHTML(id) +
        '<button class="btn btn--primary" type="button" data-add="' + id + '">' + esc(t('add_to_cart')) + '</button>' +
        '<button class="btn btn--ghost" type="button" data-quick-buy="' + id + '">' + esc(t('cart_checkout')) + '</button>' +
      '</div>' +
      '<p class="note">' + esc(t('d_delivery')) + '</p><p class="disclaimer">' + esc(t('d_disclaimer')) + '</p>' +
      '</div></article>';
  }
  function stepperHTML(id) {
    return '<div class="stepper" role="group" aria-label="' + esc(t('qty')) + '"><button type="button" data-dec aria-label="−">−</button>' +
      '<output aria-live="polite">1</output><button type="button" data-inc aria-label="+">+</button></div>';
  }
  function renderDetails() {
    $('#detailsRoot').innerHTML = ['mane', 'cord', 'dual'].map(detailHTML).join('');
  }

  /* ---------- cart ---------- */
  function lineThumb(id) {
    return id === 'dual'
      ? '<div class="line__thumb" style="display:flex;gap:2px"><div class="bottle" data-bottle="mane" style="--bw:28px"></div><div class="bottle" data-bottle="cord" style="--bw:28px"></div></div>'
      : '<div class="line__thumb"><div class="bottle" data-bottle="' + id + '" style="--bw:40px"></div></div>';
  }
  function summaryHTML(c) {
    return '<div class="sum"><div><span>' + esc(t('cart_subtotal')) + '</span><span>' + gel(c.subtotal) + '</span></div>' +
      '<div class="' + (c.discount ? 'disc' : '') + '"><span>' + esc(t('cart_discount')) + '</span><span>−' + gel(c.discount) + '</span></div>' +
      '<div class="tot"><span>' + esc(t('cart_total')) + '</span><span>' + gel(c.total) + '</span></div></div>';
  }
  function renderCart() {
    var items = cart.asItems(), calc = Pricing.calculateCart(items);
    var badge = $('#cartCount'); badge.textContent = calc.bottles; badge.hidden = calc.bottles === 0;

    var sticky = $('#stickyCart');
    if (sticky) {
      sticky.hidden = calc.bottles === 0;
      var sc = $('#stickyCount'), st = $('#stickyTotal');
      if (sc) sc.textContent = calc.bottles + ' ' + t('cart_bottles');
      if (st) st.textContent = gel(calc.total);
    }

    var body = $('#cartBody'), foot = $('#cartFoot');
    if (!items.length) {
      body.innerHTML = '<p class="empty">' + esc(t('cart_empty')) + '</p>';
      foot.innerHTML = '<button class="btn btn--ghost btn--block" type="button" data-close-cart>' + esc(t('cart_continue')) + '</button>';
    } else {
      body.innerHTML = (calc.bottlesToDiscount ? '<div class="hint" role="status">' + esc(t('cart_hint')) + '</div>' : '') +
        items.map(function (it) {
          var line = Pricing.calculateCart([it]).subtotal;
          return '<div class="line">' + lineThumb(it.id) + '<div><h3>' + esc(pname(it.id)) + '</h3>' +
            (it.id === 'dual' ? '<small>' + esc(t('cart_set_of')) + '</small>' : '') +
            '<div class="stepper" role="group" aria-label="' + esc(t('qty')) + '"><button type="button" data-line-dec="' + it.id + '" aria-label="−">−</button><output>' + it.qty +
            '</output><button type="button" data-line-inc="' + it.id + '" aria-label="+">+</button></div></div>' +
            '<div class="line__price">' + gel(line) + '<button class="line__rm" type="button" data-line-rm="' + it.id + '">' + esc(t('cart_remove')) + '</button></div></div>';
        }).join('');
      foot.innerHTML = summaryHTML(calc) + '<p class="note" style="margin:12px 0">' + esc(t('cart_free')) + '</p>' +
        '<button class="btn btn--primary btn--block" type="button" data-checkout>' + esc(t('cart_checkout')) + '</button>' +
        '<button class="btn btn--ghost btn--block" type="button" data-close-cart style="margin-top:10px">' + esc(t('cart_continue')) + '</button>';
    }
    renderBottles(body);
    $('#checkoutSum').innerHTML = summaryHTML(calc);
  }

  var dlg = $('#cartDialog');
  function showView(name) {
    $$('.view', dlg).forEach(function (v) { v.hidden = v.getAttribute('data-view') !== name; });
    if (name === 'checkout') {
      var calc = Pricing.calculateCart(cart.asItems());
      trackEvent('begin_checkout', { currency: 'GEL', value: calc.total });
      var first = $('#f-name'); if (first) first.focus();
    }
  }
  function openCart(view) {
    if (!dlg.open) {
      if (typeof dlg.showModal === 'function') dlg.showModal();
      else dlg.setAttribute('open', '');
      document.body.classList.add('no-scroll');
    }
    showView(view || 'cart');
  }
  function closeCart() { if (dlg.open) dlg.close(); }
  dlg.addEventListener('close', function () {
    document.body.classList.remove('no-scroll');
    if (!$('.view[data-view="done"]', dlg).hidden) { doneState = null; showView('cart'); }
  });
  dlg.addEventListener('click', function (e) { if (e.target === dlg) closeCart(); });

  /* ---------- checkout ---------- */
  function renderConsent() {
    $('#consentText').innerHTML = esc(t('f_consent')).replace('{privacy}', '<a href="/legal#privacy" target="_blank" rel="noopener">' + esc(t('f_privacy')) + '</a>');
  }
  var FIELDS = ['name', 'phone', 'email', 'city', 'address', 'consent'];
  function setErr(id, key) {
    var input = $('#f-' + id), box = $('#err-' + id);
    if (input) input.setAttribute('aria-invalid', key ? 'true' : 'false');
    if (box) box.textContent = key ? t(key) : '';
  }
  function validate() {
    var v = function (id) { return ($('#f-' + id).value || '').trim(); };
    var errs = {
      name: v('name').length < 2 ? 'err_required' : '',
      phone: !v('phone') ? 'err_required' : (!PHONE_RE.test(v('phone')) ? 'err_phone' : ''),
      email: !v('email') ? 'err_required' : (!EMAIL_RE.test(v('email')) ? 'err_email' : ''),
      city: v('city').length < 2 ? 'err_required' : '',
      address: v('address').length < 5 ? 'err_required' : '',
      consent: $('#f-consent').checked ? '' : 'err_consent'
    };
    var firstBad = null;
    FIELDS.forEach(function (f) { setErr(f, errs[f]); if (errs[f] && !firstBad) firstBad = f; });
    if (firstBad) $('#f-' + firstBad).focus();
    return !firstBad;
  }
  function formAlert(key) {
    var a = $('#formAlert');
    a.hidden = !key; a.textContent = key ? t(key) : '';
  }
  function submitOrder(e) {
    e.preventDefault();
    formAlert('');
    if (!validate()) return;
    var items = cart.asItems();
    if (!items.length) { showView('cart'); return; }
    var btn = $('#submitBtn');
    btn.disabled = true; btn.textContent = t('f_sending');
    var ctrl = window.AbortController ? new AbortController() : null;
    var timer = setTimeout(function () { if (ctrl) ctrl.abort(); }, 20000);
    fetch('/api/order', {
      method: 'POST', headers: { 'Content-Type': 'application/json' }, signal: ctrl ? ctrl.signal : undefined,
      body: JSON.stringify({
        items: items,
        name: $('#f-name').value,
        phone: $('#f-phone').value,
        email: $('#f-email').value,
        city: $('#f-city').value,
        address: $('#f-address').value,
        contact_method: $('#f-method').value,
        contact_handle: $('#f-handle').value,
        consent: $('#f-consent').checked,
        lang: lang,
        website: $('#f-website').value
      })
    }).then(function (res) {
      return res.json().then(function (data) { return { status: res.status, data: data }; });
    }).then(function (r) {
      if (r.status === 429) return formAlert('err_rate');
      if (!r.data || !r.data.ok) {
        var e2 = r.data && r.data.error;
        if (e2 === 'bad phone') setErr('phone', 'err_phone');
        if (e2 === 'bad email') setErr('email', 'err_email');
        return formAlert('err_generic');
      }
      doneState = r.data;
      trackEvent('purchase', {
        transaction_id: String(r.data.order_id),
        currency: 'GEL',
        value: r.data.totals ? r.data.totals.total : 0,
        items: items.map(function (it) { return { item_id: it.id, item_name: pname(it.id), quantity: it.qty }; })
      });
      cart.clear();
      $('#orderForm').reset();
      renderDone();
      showView('done');
    }).catch(function () { formAlert('err_network'); })
      .then(function () { clearTimeout(timer); btn.disabled = false; btn.textContent = t('f_submit'); });
  }

  /* ---------- order confirmation (directs customer to Telegram bot to choose TBC or Crypto) ---------- */
  function renderDone() {
    var d = doneState; if (!d) return;
    var html = '<h3 style="font-size:26px;margin-bottom:6px">' + esc(t('done_title')) + '</h3>' +
      '<p class="note">' + esc(t('done_order')) + ' <b style="color:var(--amber);font-family:var(--mono)">#' + esc(d.order_id) + '</b></p>';
    html += d.notified
      ? '<div class="alert alert--ok">' + esc(t('done_ok')) + '</div>'
      : '<div class="alert alert--warn"><b>' + esc(t('done_warn_title')) + '</b><br>' + esc(t('done_warn')) + '</div>';
    if (d.totals && d.totals.total !== undefined) {
      html += '<div style="margin:18px 0">' + summaryHTML(d.totals) + '</div>';
    }
    html += '<h4 style="font:700 12px/1 var(--mono);letter-spacing:.16em;text-transform:uppercase;color:var(--amber);margin:20px 0 8px">' + esc(t('done_pay')) + '</h4>';
    if (d.bot_link) {
      html += '<p class="note" style="margin-bottom:14px">' + esc(t('done_pay_bot_hint')) + '</p>';
      html += '<a class="btn btn--primary btn--block" id="tgPayBtn" target="_blank" rel="noopener" href="' + esc(d.bot_link) + '">✈️ ' + esc(t('done_tg')) + '</a>';
    } else if (d.requisites) {
      html += '<code class="req">' + esc(d.requisites) + '</code>';
    } else {
      html += '<p class="note">' + esc(t('done_pay_none')) + '</p>';
    }
    if (!d.notified || !d.bot_link) {
      var msg = encodeURIComponent('Mind Root — order #' + d.order_id + (d.totals ? ', ' + d.totals.total + ' GEL' : ''));
      var tg = d.owner_telegram ? 'https://t.me/' + encodeURIComponent(d.owner_telegram) + '?text=' + msg : SITE.contact.telegramUrl;
      if (tg) html += '<a class="btn btn--ghost btn--block" style="margin-top:10px" target="_blank" rel="noopener" href="' + esc(tg) + '">' + esc(t('done_owner')) + '</a>';
      html += '<a class="btn btn--ghost btn--block" style="margin-top:10px" target="_blank" rel="noopener" href="' + esc(SITE.contact.instagramUrl) + '">' + esc(t('done_ig')) + '</a>';
    }
    html += '<button class="btn btn--ghost btn--block" style="margin-top:10px" type="button" data-close-cart>' + esc(t('done_close')) + '</button>';
    $('#doneBody').innerHTML = html;
  }

  /* ---------- events (delegated) ---------- */
  document.addEventListener('click', function (e) {
    var el = e.target.closest('button, a');
    if (!el) return;
    var wrap = el.closest('[role="group"].stepper, .stepper');
    if (el.hasAttribute('data-inc') || el.hasAttribute('data-dec')) {
      var out = $('output', wrap), n = parseInt(out.textContent, 10) || 1;
      n += el.hasAttribute('data-inc') ? 1 : -1;
      out.textContent = Math.max(1, Math.min(MAX_QTY, n));
    } else if (el.hasAttribute('data-add')) {
      var addId = el.getAttribute('data-add');
      var row = el.closest('.card__footer, .card__row, .detail__cta'), outEl = row ? $('output', row) : null;
      var q = outEl ? (parseInt(outEl.textContent, 10) || 1) : 1;
      cart.add(addId, q);
      trackEvent('add_to_cart', {
        currency: 'GEL',
        value: Pricing.calculateCart([{ id: addId, qty: q }]).total,
        items: [{ item_id: addId, item_name: pname(addId), quantity: q }]
      });
      if (outEl) outEl.textContent = '1';
      openCart('cart');
    } else if (el.hasAttribute('data-quick-buy')) {
      var qId = el.getAttribute('data-quick-buy');
      var qRow = el.closest('.card__footer, .detail__cta'), qOut = qRow ? $('output', qRow) : null;
      var qCount = qOut ? (parseInt(qOut.textContent, 10) || 1) : 1;
      if (cart.qty(qId) === 0) {
        cart.add(qId, qCount);
        trackEvent('add_to_cart', {
          currency: 'GEL',
          value: Pricing.calculateCart([{ id: qId, qty: qCount }]).total,
          items: [{ item_id: qId, item_name: pname(qId), quantity: qCount }]
        });
      }
      if (qOut) qOut.textContent = '1';
      openCart('checkout');
    } else if (el.id === 'tgPayBtn') {
      trackEvent('open_telegram_payment', { order_id: doneState ? String(doneState.order_id) : '' });
    } else if (el.hasAttribute('data-open-cart-view')) {
      openCart(el.getAttribute('data-open-cart-view'));
    } else if (el.hasAttribute('data-line-inc')) cart.add(el.getAttribute('data-line-inc'), 1);
    else if (el.hasAttribute('data-line-dec')) { var id = el.getAttribute('data-line-dec'); cart.set(id, cart.qty(id) - 1); }
    else if (el.hasAttribute('data-line-rm')) cart.remove(el.getAttribute('data-line-rm'));
    else if (el.hasAttribute('data-checkout')) openCart('checkout');
    else if (el.hasAttribute('data-back-cart')) showView('cart');
    else if (el.hasAttribute('data-close-cart') || el.id === 'closeCart') closeCart();
    else if (el.id === 'openCart' || el.id === 'openCartAbout') openCart('cart');
    else if (el.hasAttribute('data-lang')) setLang(el.getAttribute('data-lang'));
    else if (el.id === 'burger') toggleMenu();
    else if (el.closest('#nav') && el.tagName === 'A') toggleMenu(false);
  });
  $('#orderForm').addEventListener('submit', submitOrder);
  cart.subscribe(renderCart);

  function toggleMenu(force) {
    var nav = $('#nav'), b = $('#burger');
    var open = force === undefined ? !nav.classList.contains('is-open') : force;
    nav.classList.toggle('is-open', open);
    $('.site-header').classList.toggle('menu-open', open);
    b.setAttribute('aria-expanded', String(open));
  }
  function onScroll() { $('.site-header').classList.toggle('is-solid', window.scrollY > 40); }
  window.addEventListener('scroll', onScroll, { passive: true });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') toggleMenu(false); });

  onScroll();
  setLang(lang);
})();