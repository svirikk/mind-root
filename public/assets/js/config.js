/* ==========================================================================
   Mind Root — EDIT ME. Everything the owner is likely to change lives here
   (contacts, delivery, quality-document links, label facts). Copy and the
   three languages live in i18n.js. Prices live in pricing.js (and pricing.py
   on the server — change both together, then run the tests).
   Values in [square brackets] are placeholders: fill them in, or leave them
   and the site shows them as visible "to be completed" text.
   ========================================================================== */
window.SITE = {
  contact: {
    email: "[hello@your-domain.ge]",
    phone: "[+995 5XX XX XX XX]",
    instagramHandle: "@mindroot.ge",
    instagramUrl: "https://instagram.com/mindroot.ge",
    telegramHandle: "[@your_telegram]",
    telegramUrl: "",                 // e.g. "https://t.me/your_telegram"
    place: "Batumi, Georgia"
  },
  delivery: { feeGel: 0, daysMin: 1, daysMax: 3 },   // free, 1–3 days after payment is confirmed
  // Links to PDF documents. Leave "" to show "available on request".
  docs: { coaMane: "", coaCord: "", halal: "" },
  // Facts copied from the real label (English, as printed).
  label: {
    capsules: 120,
    servingSize: "2 capsules",
    servings: 60,
    otherIngredients: "Vegetable Cellulose (Capsule), Rice Flour, Magnesium Stearate (Plant Source)",
    suggestedUse: "As a dietary supplement, take 2 capsules one to two times per day, preferably with a meal, or as directed by your healthcare professional.",
    storage: "Store in a cool, dry place away from direct light. Keep out of reach of children.",
    origin: "Manufactured in China. Distributed by Mind Root, Batumi, Georgia.",
    batch: "[batch no. / best-before — add when stock arrives]"
  },
  products: {
    mane: { name: "Lion's Mane", latin: "Hericium erinaceus", ratio: "10:1", part: "Fruiting body", amount: "1000 mg", label: "/assets/img/label-mane.jpg" },
    cord: { name: "Cordyceps", latin: "Cordyceps militaris", ratio: "8:1", part: "Fruiting body", amount: "1000 mg", label: "/assets/img/label-cord.jpg" }
  }
};
