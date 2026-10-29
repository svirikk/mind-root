const assert = require('assert');
const CartStore = require('../public/assets/js/cart.js');
const Pricing = require('../public/assets/js/pricing.js');

const mem = () => { const m = {}; return { getItem: k => (k in m ? m[k] : null), setItem: (k, v) => { m[k] = String(v); }, _m: m }; };

let s = mem(); let c = CartStore.create(s);
c.add('mane'); c.add('mane'); c.add('dual');
assert.deepStrictEqual(c.asItems(), [{ id: 'mane', qty: 2 }, { id: 'dual', qty: 1 }]);
assert.strictEqual(Pricing.calculateCart(c.asItems()).total, 256);        // 2 + 2 = 4 bottles
// persistence: a new cart over the same storage sees the same state
assert.deepStrictEqual(CartStore.create(s).asItems(), c.asItems());
c.set('mane', 0); assert.strictEqual(c.qty('mane'), 0);
c.set('cord', 999); assert.strictEqual(c.qty('cord'), CartStore.MAX);       // clamped
c.add('nope'); assert.strictEqual(c.qty('nope'), 0);                        // unknown ids ignored
c.remove('cord'); c.clear(); assert.deepStrictEqual(c.asItems(), []);
// corrupted / hostile storage never crashes and never yields bad quantities
const bad = mem(); bad.setItem(CartStore.KEY, '{"mane":-3,"cord":"2","dual":1.5,"x":4}');
assert.deepStrictEqual(CartStore.create(bad).asItems(), []);
bad.setItem(CartStore.KEY, 'not json'); assert.deepStrictEqual(CartStore.create(bad).asItems(), []);
assert.deepStrictEqual(CartStore.create(null).asItems(), []);               // no storage at all
let n = 0; const c2 = CartStore.create(mem()); c2.subscribe(() => n++); c2.add('mane'); c2.add('cord'); assert.strictEqual(n, 2);
console.log('cart.js: OK');
