/* Mind Root — CartStore (UMD: works in browser as window.CartStore and in Node tests). */
(function (root, factory) {
    if (typeof module === 'object' && module.exports) module.exports = factory();
    else root.CartStore = factory();
  })(typeof self !== 'undefined' ? self : this, function () {
    'use strict';
  
    var KEY = 'mindroot_cart';
    var MAX = 20;
    var VALID_IDS = ['mane', 'cord', 'dual'];
  
    function isValidId(id) {
      return VALID_IDS.indexOf(id) !== -1;
    }
  
    function clampQty(n) {
      if (typeof n !== 'number' || !Number.isInteger(n) || n <= 0) return 0;
      return Math.min(MAX, n);
    }
  
    function create(storage) {
      var state = {};
      var listeners = [];
  
      function load() {
        state = {};
        if (!storage || typeof storage.getItem !== 'function') return;
        try {
          var raw = storage.getItem(KEY);
          if (!raw) return;
          var parsed = JSON.parse(raw);
          if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) return;
  
          var keys = Object.keys(parsed);
          for (var i = 0; i < keys.length; i++) {
            var k = keys[i];
            var v = parsed[k];
            // If any entry in stored JSON is hostile/corrupted, reject the corrupted payload safely
            if (!isValidId(k) || typeof v !== 'number' || !Number.isInteger(v) || v < 0) {
              state = {};
              return;
            }
            if (v > 0) state[k] = Math.min(MAX, v);
          }
        } catch (e) {
          state = {};
        }
      }
  
      function save() {
        if (!storage || typeof storage.setItem !== 'function') return;
        try {
          storage.setItem(KEY, JSON.stringify(state));
        } catch (e) { /* ignore quota errors */ }
      }
  
      function notify() {
        for (var i = 0; i < listeners.length; i++) {
          try { listeners[i](api); } catch (e) { /* ignore listener errors */ }
        }
      }
  
      load();
  
      var api = {
        qty: function (id) {
          return isValidId(id) && state[id] ? state[id] : 0;
        },
        add: function (id, amount) {
          if (!isValidId(id)) return;
          var step = amount === undefined ? 1 : amount;
          if (typeof step !== 'number' || !Number.isInteger(step) || step <= 0) return;
          var next = (state[id] || 0) + step;
          state[id] = Math.min(MAX, next);
          save();
          notify();
        },
        set: function (id, qty) {
          if (!isValidId(id)) return;
          if (typeof qty !== 'number' || !Number.isInteger(qty) || qty <= 0) {
            delete state[id];
          } else {
            state[id] = clampQty(qty);
          }
          save();
          notify();
        },
        remove: function (id) {
          if (state[id]) {
            delete state[id];
            save();
            notify();
          }
        },
        clear: function () {
          state = {};
          save();
          notify();
        },
        asItems: function () {
          var out = [];
          for (var i = 0; i < VALID_IDS.length; i++) {
            var id = VALID_IDS[i];
            if (state[id] && state[id] > 0) {
              out.push({ id: id, qty: state[id] });
            }
          }
          return out;
        },
        subscribe: function (fn) {
          if (typeof fn === 'function') listeners.push(fn);
          return function unsubscribe() {
            var idx = listeners.indexOf(fn);
            if (idx !== -1) listeners.splice(idx, 1);
          };
        }
      };
  
      return api;
    }
  
    return {
      KEY: KEY,
      MAX: MAX,
      VALID_IDS: VALID_IDS,
      create: create
    };
  });