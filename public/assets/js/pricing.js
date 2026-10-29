/* Pricing rules — integer GEL only. Mirrored on the server in pricing.py (same test table).
 * Rule: every bottle costs UNIT_PRICE. With 2+ bottles in the cart, 20% off the whole bottle subtotal.
 * "dual" (Dual Complex) = 1 Lion's Mane + 1 Cordyceps = 2 bottles. Discount is computed ONCE on the
 * total bottle count, so the bundle can never be discounted twice (dual alone = 2 bottles = 128). */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.Pricing = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  var UNIT_PRICE = 80;          // GEL per bottle
  var DISCOUNT_PERCENT = 20;
  var MIN_BOTTLES_FOR_DISCOUNT = 2;
  var BOTTLES_PER_ITEM = { mane: 1, cord: 1, dual: 2 };

  function calculateCart(items) {
    var bottles = 0;
    (items || []).forEach(function (it) {
      var per = BOTTLES_PER_ITEM[it.id];
      var qty = it.qty;
      if (!per || !Number.isInteger(qty) || qty < 0) throw new Error('invalid cart item');
      bottles += per * qty;
    });
    var subtotal = bottles * UNIT_PRICE;
    var discount = bottles >= MIN_BOTTLES_FOR_DISCOUNT ? (subtotal * DISCOUNT_PERCENT) / 100 : 0;
    return {
      bottles: bottles,
      subtotal: subtotal,
      discount: discount,
      total: subtotal - discount,
      discountApplied: discount > 0,
      bottlesToDiscount: bottles >= MIN_BOTTLES_FOR_DISCOUNT ? 0 : MIN_BOTTLES_FOR_DISCOUNT - bottles
    };
  }

  return {
    UNIT_PRICE: UNIT_PRICE, DISCOUNT_PERCENT: DISCOUNT_PERCENT, BOTTLES_PER_ITEM: BOTTLES_PER_ITEM,
    MIN_BOTTLES_FOR_DISCOUNT: MIN_BOTTLES_FOR_DISCOUNT, calculateCart: calculateCart
  };
});
