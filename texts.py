# -*- coding: utf-8 -*-
"""All user-facing strings, per language. Edit freely without touching bot.py logic."""

PRODUCTS = {
    "mane": {"price": 80, "emoji": "🧠"},
    "cord": {"price": 80, "emoji": "⚡"},
    "bundle": {"price": 128, "emoji": "🍄"},
}

LANGS = ["en", "ka", "uk"]

LANG_BUTTON_LABELS = {
    "en": "English",
    "ka": "ქართული",
    "uk": "Українська",
}

T = {
"en": {
    "choose_lang": "Please select your language:",
    "welcome": (
        "Hi! I'm Bogdan, the Mind Root order bot 🍄\n\n"
        "Tap a product below to order, or \"Learn more\" for details.\n"
        "Delivery across Georgia, payment by card.\n\nHappy shopping!"
    ),
    "name": {"mane": "Lion's Mane", "cord": "Cordyceps", "bundle": "Lion's Mane + Cordyceps (set)"},
    "tagline": {
        "mane": "Memory / Focus / Nerve Support",
        "cord": "Energy / Endurance / Vitality",
        "bundle": "The complete daily ritual — both products, free shipping",
    },
    "learn_more_btn": "ℹ️ Learn more",
    "order_btn": "🛒 Order",
    "back_btn": "⬅️ Back",
    "details": {
        "mane": (
            "🧠 *Lion's Mane Mushroom*\n\n"
            "Lion's Mane (Hericium erinaceus) is a functional mushroom traditionally valued for its "
            "potential to support cognitive health, focus and nerve function.\n\n"
            "*Composition:* Lion's Mane Mushroom Extract 10:1 (Fruiting Body), 1000 mg per serving (2 capsules)\n"
            "*Other ingredients:* Vegetable Cellulose (Capsule), Rice Flour, Magnesium Stearate (Plant Source)\n"
            "*Suggested use:* 2 capsules, 1–2 times per day, preferably with a meal\n"
            "*120 capsules per bottle — up to 4 months' supply*\n\n"
            "*Caution:* Do not exceed recommended dose. Pregnant or nursing women, children under 18, "
            "and individuals with a medical condition or taking medication should consult a healthcare "
            "professional before use. This product is a dietary supplement and is not intended to "
            "diagnose, treat, cure, or prevent any disease.\n\n"
            "*Price: 80 ₾*"
        ),
        "cord": (
            "⚡ *Cordyceps Mushroom*\n\n"
            "Cordyceps is a traditional functional mushroom valued for its potential to support energy, "
            "stamina and overall vitality.\n\n"
            "*Composition:* Cordyceps Mushroom Extract 8:1 (Fruiting Body, Cordyceps militaris), 1000 mg per serving (2 capsules)\n"
            "*Other ingredients:* Vegetable Cellulose (Capsule), Rice Flour, Magnesium Stearate (Plant Source)\n"
            "*Suggested use:* 2 capsules, 1–2 times per day, preferably with a meal\n"
            "*120 capsules per bottle — up to 4 months' supply*\n\n"
            "*Caution:* Do not exceed recommended dose. Pregnant or nursing women, children under 18, "
            "and individuals with a medical condition or taking medication should consult a healthcare "
            "professional before use. This product is a dietary supplement and is not intended to "
            "diagnose, treat, cure, or prevent any disease.\n\n"
            "*Price: 80 ₾*"
        ),
        "bundle": (
            "🍄 *Lion's Mane + Cordyceps — Set*\n\n"
            "Both products in one order — free shipping included, and cheaper than buying separately.\n\n"
            "*Price: 128 ₾ (instead of 160 ₾), free delivery*"
        ),
    },
    "ask_details": (
        "Great choice! Please send me, *all in one message*:\n\n"
        "📞 Phone number\n🏙 City\n🏠 Delivery address\n🧾 Full name\n\n"
        "Example:\n+995 555 123456\nBatumi\nKhimshiashvili str. 12\nGiorgi Giorgadze"
    ),
    "order_created": (
        "Thank you for your order! 🙏\n\n"
        "*Order #{order_id}*\nTotal: *{price} ₾*\n\n"
        "Please transfer the amount to:\n`{requisites}`\n\n"
        "Once paid, please send a screenshot of the payment right here 🥰"
    ),
    "ask_screenshot_again": "Please send a screenshot of your payment confirmation 📸",
    "reminder": (
        "Hi! Just a friendly reminder about *order #{order_id}* ({price} ₾).\n"
        "Requisites: `{requisites}`\nWe'll process it as soon as we receive your payment confirmation 🙂"
    ),
    "invalid_receipt": (
        "Hmm, this screenshot doesn't look right 🤔 Could you please send a clear screenshot of the "
        "payment confirmation for order #{order_id}?"
    ),
    "paid_confirmed": (
        "Payment confirmed! ✅\n\nThank you for your order, it's now being processed and will be shipped soon.\n"
        "Estimated delivery: 1–3 days 🚚"
    ),
    "screenshot_received": "Got it! We'll check your payment and confirm shortly 🙏",
    "question_forwarded": "Thanks, your message has been sent — we'll get back to you shortly 🙂",
},
"ka": {
    "choose_lang": "გთხოვთ აირჩიოთ ენა:",
    "welcome": (
        "გამარჯობა! მე ბოგდანი ვარ, Mind Root-ის შეკვეთების ბოტი 🍄\n\n"
        "დააჭირეთ პროდუქტს შესაკვეთად, ან „გაიგეთ მეტი“ დეტალებისთვის.\n"
        "მიწოდება საქართველოს მასშტაბით, გადახდა ბარათით.\n\nსასიამოვნო შოპინგს გისურვებთ!"
    ),
    "name": {"mane": "Lion's Mane", "cord": "Cordyceps", "bundle": "Lion's Mane + Cordyceps (კომპლექტი)"},
    "tagline": {
        "mane": "მეხსიერება / ფოკუსი / ნერვების მხარდაჭერა",
        "cord": "ენერგია / გამძლეობა / სასიცოცხლო ძალა",
        "bundle": "სრული ყოველდღიური რიტუალი — ორივე პროდუქტი, უფასო მიწოდება",
    },
    "learn_more_btn": "ℹ️ გაიგეთ მეტი",
    "order_btn": "🛒 შეკვეთა",
    "back_btn": "⬅️ უკან",
    "details": {
        "mane": (
            "🧠 *Lion's Mane Mushroom*\n\n"
            "Lion's Mane (Hericium erinaceus) — ფუნქციური სოკო, რომელიც ტრადიციულად გამოიყენება "
            "გონებრივი სიცხადის, ფოკუსისა და ნერვული სისტემის მხარდასაჭერად.\n\n"
            "*შემადგენლობა:* Lion's Mane ექსტრაქტი 10:1 (Fruiting Body), 1000 მგ ულუფაზე (2 კაფსულა)\n"
            "*სხვა ინგრედიენტები:* მცენარეული ცელულოზა (კაფსულა), ბრინჯის ფქვილი, მაგნიუმის სტეარატი\n"
            "*რეკომენდებული მიღება:* 2 კაფსულა, დღეში 1–2-ჯერ, სასურველია საკვებთან ერთად\n"
            "*120 კაფსულა ქილაში — დაახლ. 4 თვის მარაგი*\n\n"
            "*გაფრთხილება:* არ გადააჭარბოთ რეკომენდებულ დოზას. ორსულობის, ძუძუთი კვების, 18 წლამდე "
            "ასაკის ან ქრონიკული დაავადების შემთხვევაში მიმართეთ ექიმს. ეს პროდუქტი არის კვებითი "
            "დანამატი და არ არის განკუთვნილი რაიმე დაავადების დიაგნოსტირების ან მკურნალობისთვის.\n\n"
            "*ფასი: 80 ₾*"
        ),
        "cord": (
            "⚡ *Cordyceps Mushroom*\n\n"
            "Cordyceps — ტრადიციული ფუნქციური სოკო, რომელიც გამოიყენება ენერგიის, გამძლეობისა და "
            "საერთო სასიცოცხლო ტონუსის მხარდასაჭერად.\n\n"
            "*შემადგენლობა:* Cordyceps ექსტრაქტი 8:1 (Fruiting Body, Cordyceps militaris), 1000 მგ ულუფაზე (2 კაფსულა)\n"
            "*სხვა ინგრედიენტები:* მცენარეული ცელულოზა (კაფსულა), ბრინჯის ფქვილი, მაგნიუმის სტეარატი\n"
            "*რეკომენდებული მიღება:* 2 კაფსულა, დღეში 1–2-ჯერ, სასურველია საკვებთან ერთად\n"
            "*120 კაფსულა ქილაში — დაახლ. 4 თვის მარაგი*\n\n"
            "*გაფრთხილება:* არ გადააჭარბოთ რეკომენდებულ დოზას. ორსულობის, ძუძუთი კვების, 18 წლამდე "
            "ასაკის ან ქრონიკული დაავადების შემთხვევაში მიმართეთ ექიმს. ეს პროდუქტი არის კვებითი "
            "დანამატი და არ არის განკუთვნილი რაიმე დაავადების დიაგნოსტირების ან მკურნალობისთვის.\n\n"
            "*ფასი: 80 ₾*"
        ),
        "bundle": (
            "🍄 *Lion's Mane + Cordyceps — კომპლექტი*\n\n"
            "ორივე პროდუქტი ერთ შეკვეთაში — უფასო მიწოდებით და იაფად, ვიდრე ცალ-ცალკე ყიდვა.\n\n"
            "*ფასი: 128 ₾ (160 ₾-ის ნაცვლად), უფასო მიწოდება*"
        ),
    },
    "ask_details": (
        "მშვენიერი არჩევანია! გთხოვთ გამომიგზავნოთ *ერთ შეტყობინებაში*:\n\n"
        "📞 ტელეფონის ნომერი\n🏙 ქალაქი\n🏠 მიწოდების მისამართი\n🧾 სახელი და გვარი\n\n"
        "მაგალითად:\n+995 555 123456\nბათუმი\nხიმშიაშვილის ქ. 12\nგიორგი გიორგაძე"
    ),
    "order_created": (
        "მადლობა შეკვეთისთვის! 🙏\n\n"
        "*შეკვეთა #{order_id}*\nჯამი: *{price} ₾*\n\n"
        "გთხოვთ გადარიცხოთ თანხა:\n`{requisites}`\n\n"
        "გადახდის შემდეგ, გთხოვთ გამომიგზავნოთ ეკრანის სურათი 🥰"
    ),
    "ask_screenshot_again": "გთხოვთ გამომიგზავნოთ გადახდის დამადასტურებელი სქრინშოთი 📸",
    "reminder": (
        "გამარჯობა! შეგახსენებთ *შეკვეთას #{order_id}* ({price} ₾).\n"
        "რეკვიზიტები: `{requisites}`\nდავამუშავებთ გადახდის დადასტურებისთანავე 🙂"
    ),
    "invalid_receipt": (
        "სქრინშოთი არ ჩანს სწორად 🤔 გთხოვთ გამომიგზავნოთ გადახდის მკაფიო სქრინშოთი შეკვეთისთვის #{order_id}"
    ),
    "paid_confirmed": (
        "გადახდა დადასტურებულია! ✅\n\nმადლობა შეკვეთისთვის, მალე გამოიგზავნება.\n"
        "სავარაუდო მიწოდება: 1–3 დღე 🚚"
    ),
    "screenshot_received": "მივიღეთ! შევამოწმებთ გადახდას და მალე დავადასტურებთ 🙏",
    "question_forwarded": "მადლობა, შეტყობინება გაგზავნილია — მალე დაგიკავშირდებით 🙂",
},
"uk": {
    "choose_lang": "Будь ласка, оберіть мову:",
    "welcome": (
        "Привіт! Я — бот Богдан, бот замовлень Mind Root 🍄\n\n"
        "Тисніть на товар, щоб замовити, або «Дізнатися більше» для деталей.\n"
        "Доставка по всій Грузії, оплата карткою.\n\nПриємних покупок!"
    ),
    "name": {"mane": "Lion's Mane", "cord": "Cordyceps", "bundle": "Lion's Mane + Cordyceps (набір)"},
    "tagline": {
        "mane": "Пам'ять / Фокус / Підтримка нервової системи",
        "cord": "Енергія / Витривалість / Життєвий тонус",
        "bundle": "Повний щоденний ритуал — обидва продукти, безкоштовна доставка",
    },
    "learn_more_btn": "ℹ️ Дізнатися більше",
    "order_btn": "🛒 Замовити",
    "back_btn": "⬅️ Назад",
    "details": {
        "mane": (
            "🧠 *Lion's Mane Mushroom*\n\n"
            "Lion's Mane (Hericium erinaceus) — функціональний гриб, який традиційно застосовують для "
            "підтримки когнітивного здоров'я, фокусу та нервової системи.\n\n"
            "*Склад:* Lion's Mane Extract 10:1 (Fruiting Body), 1000 мг на порцію (2 капсули)\n"
            "*Інші інгредієнти:* Vegetable Cellulose (капсула), рисове борошно, магнію стеарат\n"
            "*Застосування:* 2 капсули, 1–2 рази на день, бажано під час їжі\n"
            "*120 капсул у баночці — до 4 місяців прийому*\n\n"
            "*Застереження:* Не перевищувати рекомендовану дозу. Вагітним, жінкам, що годують, особам "
            "до 18 років та за наявності медичних станів — консультація лікаря. Це харчова добавка, "
            "не призначена для діагностики чи лікування захворювань.\n\n"
            "*Ціна: 80 ₾*"
        ),
        "cord": (
            "⚡ *Cordyceps Mushroom*\n\n"
            "Cordyceps — традиційний функціональний гриб, який застосовують для підтримки енергії, "
            "витривалості та загального тонусу.\n\n"
            "*Склад:* Cordyceps Extract 8:1 (Fruiting Body, Cordyceps militaris), 1000 мг на порцію (2 капсули)\n"
            "*Інші інгредієнти:* Vegetable Cellulose (капсула), рисове борошно, магнію стеарат\n"
            "*Застосування:* 2 капсули, 1–2 рази на день, бажано під час їжі\n"
            "*120 капсул у баночці — до 4 місяців прийому*\n\n"
            "*Застереження:* Не перевищувати рекомендовану дозу. Вагітним, жінкам, що годують, особам "
            "до 18 років та за наявності медичних станів — консультація лікаря. Це харчова добавка, "
            "не призначена для діагностики чи лікування захворювань.\n\n"
            "*Ціна: 80 ₾*"
        ),
        "bundle": (
            "🍄 *Lion's Mane + Cordyceps — Набір*\n\n"
            "Обидва продукти в одному замовленні — з безкоштовною доставкою і дешевше, ніж окремо.\n\n"
            "*Ціна: 128 ₾ (замість 160 ₾), безкоштовна доставка*"
        ),
    },
    "ask_details": (
        "Чудовий вибір! Надішліть, будь ласка, *одним повідомленням*:\n\n"
        "📞 Номер телефону\n🏙 Місто\n🏠 Адреса доставки\n🧾 ФІО\n\n"
        "Приклад:\n+995 555 123456\nБатумі\nвул. Хімшіашвілі 12\nІванов Іван Іванович"
    ),
    "order_created": (
        "Дякуємо за замовлення! 🙏\n\n"
        "*Замовлення #{order_id}*\nСума: *{price} ₾*\n\n"
        "Будь ласка, переведіть кошти на:\n`{requisites}`\n\n"
        "Після оплати надішліть, будь ласка, скриншот оплати сюди 🥰"
    ),
    "ask_screenshot_again": "Будь ласка, надішліть скриншот підтвердження оплати 📸",
    "reminder": (
        "Привіт! Нагадуємо про *замовлення #{order_id}* ({price} ₾).\n"
        "Реквізити: `{requisites}`\nОбробимо одразу після підтвердження оплати 🙂"
    ),
    "invalid_receipt": (
        "Хм, цей скриншот виглядає некоректно 🤔 Надішліть, будь ласка, чіткий скриншот оплати для замовлення #{order_id}"
    ),
    "paid_confirmed": (
        "Оплату підтверджено! ✅\n\nДякуємо за замовлення, воно вже в обробці та скоро буде відправлене.\n"
        "Орієнтовна доставка: 1–3 дні 🚚"
    ),
    "screenshot_received": "Отримали! Перевіримо оплату і скоро підтвердимо 🙏",
    "question_forwarded": "Дякуємо, повідомлення надіслано — скоро відповімо 🙂",
},
}
