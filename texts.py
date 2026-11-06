# -*- coding: utf-8 -*-
"""All user-facing strings, per language. Edit freely without touching bot.py logic."""

PRODUCTS = {
    "mane": {"price": 80, "emoji": "🧠"},
    "cord": {"price": 80, "emoji": "⚡"},
    "bundle": {"price": 128, "emoji": "🍄"},
}

LANGS = ["en", "uk", "ru", "ka"]

LANG_BUTTON_LABELS = {
    "en": "🇬🇧 English",
    "uk": "🇺🇦 Українська",
    "ru": "🇷🇺 Русский",
    "ka": "🇬🇪 ქართული",
}

T = {
"en": {
    "choose_lang": "Please select your language:",
    "welcome": (
        "Hi! I'm Bogdan, the Mind Root order bot 🍄\n\n"
        "Tap a product below to order, or \"Learn more\" for details.\n"
        "🚚 Free delivery across Georgia on every order!\n"
        "💳 Payment by bank transfer (TBC / BOG) or Crypto (USDT).\n\nHappy shopping!"
    ),
    "name": {"mane": "Lion's Mane", "cord": "Cordyceps", "bundle": "Dual Complex (Lion's Mane + Cordyceps)"},
    "tagline": {
        "mane": "Memory / Focus / Nerve Support",
        "cord": "Energy / Endurance / Vitality",
        "bundle": "The complete daily ritual — both bottles (−20%)",
    },
    "learn_more_btn": "ℹ️ Learn more",
    "order_btn": "🛒 Order",
    "back_btn": "⬅️ Back",
    "i_paid_btn": "✅ I have paid",
    "pay_btn_bank": "💳 Bank Transfer (TBC / BOG — GEL)",
    "pay_btn_crypto": "💎 Crypto (USDT TRC20 / BEP20)",
    "details": {
        "mane": (
            "🧠 *Lion's Mane Mushroom*\n\n"
            "Lion's Mane (Hericium erinaceus) is a functional mushroom traditionally valued for its "
            "potential to support cognitive health, focus and nerve function.\n\n"
            "*Composition:* Lion's Mane Mushroom Extract 10:1 (Fruiting Body), 1000 mg per serving (2 capsules)\n"
            "*Other ingredients:* Vegetable Cellulose (Capsule), Rice Flour, Magnesium Stearate (Plant Source)\n"
            "*Suggested use:* 2 capsules, 1–2 times per day, preferably with a meal\n"
            "*120 capsules per bottle — up to 2 months' supply*\n\n"
            "*Caution:* Do not exceed recommended dose. Pregnant or nursing women, children under 18, "
            "and individuals with a medical condition or taking medication should consult a healthcare "
            "professional before use. Dietary supplement, not a medicine.\n\n"
            "*Price: 80 ₾*"
        ),
        "cord": (
            "⚡ *Cordyceps Mushroom*\n\n"
            "Cordyceps is a traditional functional mushroom valued for its potential to support energy, "
            "stamina and overall vitality.\n\n"
            "*Composition:* Cordyceps Mushroom Extract 8:1 (Fruiting Body, Cordyceps militaris), 1000 mg per serving (2 capsules)\n"
            "*Other ingredients:* Vegetable Cellulose (Capsule), Rice Flour, Magnesium Stearate (Plant Source)\n"
            "*Suggested use:* 2 capsules, 1–2 times per day, preferably with a meal\n"
            "*120 capsules per bottle — up to 2 months' supply*\n\n"
            "*Caution:* Do not exceed recommended dose. Pregnant or nursing women, children under 18, "
            "and individuals with a medical condition or taking medication should consult a healthcare "
            "professional before use. Dietary supplement, not a medicine.\n\n"
            "*Price: 80 ₾*"
        ),
        "bundle": (
            "🍄 *Dual Complex (Lion's Mane + Cordyceps)*\n\n"
            "Both bottles in one set — 20% off automatically.\n\n"
            "*Price: 128 ₾ (instead of 160 ₾)*"
        ),
    },
    "ask_details": (
        "Great choice! Please send me, *all in one message*:\n\n"
        "📞 Phone number\n"
        "✉️ Email address (no spam — only for order & parcel pickup updates if your phone is unreachable)\n"
        "🏙 City\n"
        "🏠 Delivery address\n"
        "🧾 Full name\n\n"
        "Example:\n+995 555 123456\nname@example.com\nBatumi\nKhimshiashvili str. 12\nGiorgi Giorgadze"
    ),
    "choose_payment": (
        "Thank you! Your order *#{order_id}* is ready 🙏\n"
        "Total to pay: *{price} ₾*\n\n"
        "Please choose your preferred payment method below:"
    ),
    "bank_instructions": (
        "💳 *Bank Transfer (TBC / BOG) — Order #{order_id}*\n"
        "Amount: *{price} ₾*\n\n"
        "Please transfer the amount to:\n`{requisites}`\n\n"
        "Once transferred, tap *\"✅ I have paid\"* below (or simply send a screenshot of the receipt here) 🥰"
    ),
    "crypto_instructions": (
        "💎 *Crypto Payment (USDT) — Order #{order_id}*\n"
        "Amount: *~{usdt} USDT* ({price} ₾)\n\n"
        "*USDT (BEP20 — BNB Smart Chain, ~0$ fee):*\n`{bep20}`\n\n"
        "*USDT (TRC20 — TRON network):*\n`{trc20}`\n\n"
        "Tap the wallet address to copy it. Once sent, tap *\"✅ I have paid\"* below (or send a screenshot here) 🥰"
    ),
    "order_created": (
        "Thank you for your order! 🙏\n\n"
        "*Order #{order_id}*\nTotal: *{price} ₾*\n\n"
        "Please transfer the amount to:\n`{requisites}`\n\n"
        "Once paid, tap \"✅ I have paid\" or send a screenshot right here 🥰"
    ),
    "ask_screenshot_again": "Please tap \"✅ I have paid\" above once you transfer the funds, or send a screenshot of your payment confirmation 📸",
    "reminder": (
        "Hi! Just a friendly reminder about *order #{order_id}* ({price} ₾).\n"
        "Requisites: `{requisites}`\nWe'll process it as soon as we receive your payment confirmation 🙂"
    ),
    "invalid_receipt": (
        "Hmm, we couldn't verify the payment yet 🤔 Could you please send a clear screenshot of the "
        "payment confirmation for order #{order_id}?"
    ),
    "paid_confirmed": (
        "Payment confirmed! ✅\n\nThank you for your order, it's now being processed and will be shipped soon.\n"
        "Estimated delivery: 1–3 days 🚚"
    ),
    "screenshot_received": "Got it! We'll check your payment and confirm shortly 🙏",
    "question_forwarded": "Thanks, your message has been sent — we'll get back to you shortly 🙂",
},

"uk": {
    "choose_lang": "Будь ласка, оберіть мову / Please select your language:",
    "welcome": (
        "Привіт! Я — Богдан, бот замовлень Mind Root 🍄\n\n"
        "Тисніть на товар, щоб замовити, або «Дізнатися більше» для деталей.\n"
        "🚚 Безкоштовна доставка по всій Грузії на кожне замовлення!\n"
        "💳 Оплата на рахунок (TBC / BOG) або Криптою (USDT).\n\nПриємних покупок!"
    ),
    "name": {"mane": "Lion's Mane", "cord": "Cordyceps", "bundle": "Dual Complex (Lion's Mane + Cordyceps)"},
    "tagline": {
        "mane": "Пам'ять / Фокус / Підтримка нервової системи",
        "cord": "Енергія / Витривалість / Життєвий тонус",
        "bundle": "Повний щоденний ритуал — обидві баночки (−20%)",
    },
    "learn_more_btn": "ℹ️ Дізнатися більше",
    "order_btn": "🛒 Замовити",
    "back_btn": "⬅️ Назад",
    "i_paid_btn": "✅ Я оплатив(ла)",
    "pay_btn_bank": "💳 Картка / Рахунок Грузії (TBC / BOG — ₾)",
    "pay_btn_crypto": "💎 Крипта (USDT TRC20 / BEP20)",
    "details": {
        "mane": (
            "🧠 *Lion's Mane Mushroom*\n\n"
            "Lion's Mane (Hericium erinaceus) — функціональний гриб, який традиційно застосовують для "
            "підтримки когнітивного здоров'я, фокусу та нервової системи.\n\n"
            "*Склад:* Lion's Mane Extract 10:1 (Fruiting Body), 1000 мг на порцію (2 капсули)\n"
            "*Інші інгредієнти:* Vegetable Cellulose (капсула), рисове борошно, магнію стеарат\n"
            "*Застосування:* 2 капсули, 1–2 рази на день, бажано під час їжі\n"
            "*120 капсул у баночці — до 2 місяців прийому*\n\n"
            "*Застереження:* Не перевищувати рекомендовану дозу. Це харчова добавка, не є ліками.\n\n"
            "*Ціна: 80 ₾*"
        ),
        "cord": (
            "⚡ *Cordyceps Mushroom*\n\n"
            "Cordyceps — традиційний функціональний гриб, який застосовують для підтримки енергії, "
            "витривалості та загального тонусу.\n\n"
            "*Склад:* Cordyceps Extract 8:1 (Fruiting Body, Cordyceps militaris), 1000 мг на порцію (2 капсули)\n"
            "*Інші інгредієнти:* Vegetable Cellulose (капсула), рисове борошно, магнію стеарат\n"
            "*Застосування:* 2 капсули, 1–2 рази на день, бажано під час їжі\n"
            "*120 капсул у баночці — до 2 місяців прийому*\n\n"
            "*Застереження:* Не перевищувати рекомендовану дозу. Це харчова добавка, не є ліками.\n\n"
            "*Ціна: 80 ₾*"
        ),
        "bundle": (
            "🍄 *Dual Complex (Lion's Mane + Cordyceps)*\n\n"
            "Обидва продукти в одному замовленні — вигода 20%.\n\n"
            "*Ціна: 128 ₾ (замість 160 ₾)*"
        ),
    },
    "ask_details": (
        "Чудовий вибір! Надішліть, будь ласка, *одним повідомленням*:\n\n"
        "📞 Номер телефону\n"
        "✉️ Електронна пошта (без спаму — лише для зв'язку щодо замовлення та отримання посилки, якщо телефон поза зоною)\n"
        "🏙 Місто\n"
        "🏠 Адреса доставки\n"
        "🧾 ПІБ\n\n"
        "Приклад:\n+995 555 123456\nname@example.com\nБатумі\nвул. Хімшіашвілі 12\nІванов Іван"
    ),
    "choose_payment": (
        "Дякуємо! Ваше замовлення *#{order_id}* сформовано 🙏\n"
        "Сума до оплати: *{price} ₾*\n\n"
        "Оберіть зручний спосіб оплати нижче:"
    ),
    "bank_instructions": (
        "💳 *Оплата на рахунок (TBC / BOG) — Замовлення #{order_id}*\n"
        "Сума до переказу: *{price} ₾*\n\n"
        "Реквізити для переказу:\n`{requisites}`\n\n"
        "Після переказу натисніть кнопку *«✅ Я оплатив(ла)»* нижче (або просто надішліть сюди скриншот квитанції) 🥰"
    ),
    "crypto_instructions": (
        "💎 *Оплата Криптою (USDT) — Замовлення #{order_id}*\n"
        "Сума до переказу: *~{usdt} USDT* ({price} ₾)\n\n"
        "*Мережа BEP20 (BNB Smart Chain — комісія ~$0):*\n`{bep20}`\n\n"
        "*Мережа TRC20 (TRON):*\n`{trc20}`\n\n"
        "Натисніть на адресу гаманця, щоб скопіювати. Після переказу натисніть *«✅ Я оплатив(ла)»* нижче (або надішліть скриншот) 🥰"
    ),
    "order_created": (
        "Дякуємо за замовлення! 🙏\n\n"
        "*Замовлення #{order_id}*\nСума: *{price} ₾*\n\n"
        "Будь ласка, переведіть кошти на:\n`{requisites}`\n\n"
        "Після оплати натисніть «✅ Я оплатив(ла)» або надішліть скриншот сюди 🥰"
    ),
    "ask_screenshot_again": "Після переказу натисніть кнопку «✅ Я оплатив(ла)» вище або надішліть скриншот підтвердження оплати 📸",
    "reminder": (
        "Привіт! Нагадуємо про *замовлення #{order_id}* ({price} ₾).\n"
        "Реквізити: `{requisites}`\nОбробимо одразу після підтвердження оплати 🙂"
    ),
    "invalid_receipt": (
        "Хм, ми ще не бачимо оплату або скриншот некоректний 🤔 Надішліть, будь ласка, чіткий скриншот оплати для замовлення #{order_id}"
    ),
    "paid_confirmed": (
        "Оплату підтверджено! ✅\n\nДякуємо за замовлення, воно вже в обробці та скоро буде відправлене.\n"
        "Орієнтовна доставка: 1–3 дні 🚚"
    ),
    "screenshot_received": "Отримали! Перевіримо оплату і скоро підтвердимо 🙏",
    "question_forwarded": "Дякуємо, повідомлення надіслано — скоро відповімо 🙂",
},

"ru": {
    "choose_lang": "Пожалуйста, выберите язык:",
    "welcome": (
        "Привет! Я — Богдан, бот заказов Mind Root 🍄\n\n"
        "Нажмите на товар для заказа или «Узнать больше» для подробностей.\n"
        "🚚 Бесплатная доставка по всей Грузии на каждый заказ!\n"
        "💳 Оплата переводом (TBC / BOG) или Криптой (USDT).\n\nПриятных покупок!"
    ),
    "name": {"mane": "Lion's Mane", "cord": "Cordyceps", "bundle": "Dual Complex (Lion's Mane + Cordyceps)"},
    "tagline": {
        "mane": "Память / Фокус / Поддержка нервной системы",
        "cord": "Энергия / Выносливость / Жизненный тонус",
        "bundle": "Полный ежедневный ритуал — обе баночки (−20%)",
    },
    "learn_more_btn": "ℹ️ Узнать больше",
    "order_btn": "🛒 Заказать",
    "back_btn": "⬅️ Назад",
    "i_paid_btn": "✅ Я оплатил(а)",
    "pay_btn_bank": "💳 Карта / Счёт Грузии (TBC / BOG — ₾)",
    "pay_btn_crypto": "💎 Крипта (USDT TRC20 / BEP20)",
    "details": {
        "mane": (
            "🧠 *Lion's Mane Mushroom*\n\n"
            "Lion's Mane (Hericium erinaceus) — функциональный гриб, традиционно применяемый для "
            "поддержки когнитивного здоровья, фокуса и нервной системы.\n\n"
            "*Состав:* Lion's Mane Extract 10:1 (Fruiting Body), 1000 мг на порцию (2 капсулы)\n"
            "*Другие ингредиенты:* Vegetable Cellulose (капсула), рисовая мука, стеарат магния\n"
            "*Применение:* 2 капсулы, 1–2 раза в день, желательно во время еды\n"
            "*120 капсул в баночке — до 2 месяцев приёма*\n\n"
            "*Предостережение:* Не превышать рекомендуемую дозу. Пищевая добавка, не является лекарством.\n\n"
            "*Цена: 80 ₾*"
        ),
        "cord": (
            "⚡ *Cordyceps Mushroom*\n\n"
            "Cordyceps — традиционный функциональный гриб для поддержки энергии, "
            "выносливости и общего жизненного тонуса.\n\n"
            "*Состав:* Cordyceps Extract 8:1 (Fruiting Body, Cordyceps militaris), 1000 мг на порцию (2 капсулы)\n"
            "*Другие ингредиенты:* Vegetable Cellulose (капсула), рисовая мука, стеарат магния\n"
            "*Применение:* 2 капсулы, 1–2 раза в день, желательно во время еды\n"
            "*120 капсул в баночке — до 2 месяцев приёма*\n\n"
            "*Предостережение:* Не превышать рекомендуемую дозу. Пищевая добавка, не является лекарством.\n\n"
            "*Цена: 80 ₾*"
        ),
        "bundle": (
            "🍄 *Dual Complex (Lion's Mane + Cordyceps)*\n\n"
            "Оба продукта в одном наборе — скидка 20%.\n\n"
            "*Цена: 128 ₾ (вместо 160 ₾)*"
        ),
    },
    "ask_details": (
        "Отличный выбор! Пожалуйста, пришлите *одним сообщением*:\n\n"
        "📞 Номер телефона\n"
        "✉️ Электронная почта (без спама — только для связи по заказу и получению посылки, если телефон недоступен)\n"
        "🏙 Город\n"
        "🏠 Адрес доставки\n"
        "🧾 ФИО\n\n"
        "Пример:\n+995 555 123456\nname@example.com\nБатуми\nул. Химшиашвили 12\nИванов Иван"
    ),
    "choose_payment": (
        "Спасибо! Ваш заказ *#{order_id}* сформирован 🙏\n"
        "Сумма к оплате: *{price} ₾*\n\n"
        "Выберите удобный способ оплаты ниже:"
    ),
    "bank_instructions": (
        "💳 *Оплата переводом (TBC / BOG) — Заказ #{order_id}*\n"
        "Сумма к оплате: *{price} ₾*\n\n"
        "Реквизиты для перевода:\n`{requisites}`\n\n"
        "После перевода нажмите кнопку *«✅ Я оплатил(а)»* ниже (или просто пришлите сюда скриншот чека) 🥰"
    ),
    "crypto_instructions": (
        "💎 *Оплата Криптой (USDT) — Заказ #{order_id}*\n"
        "Сумма к переводу: *~{usdt} USDT* ({price} ₾)\n\n"
        "*Сеть BEP20 (BNB Smart Chain — комиссия ~$0):*\n`{bep20}`\n\n"
        "*Сеть TRC20 (TRON):*\n`{trc20}`\n\n"
        "Нажмите на адрес кошелька, чтобы скопировать. После перевода нажмите *«✅ Я оплатил(а)»* ниже (или отправьте скриншот) 🥰"
    ),
    "order_created": (
        "Спасибо за заказ! 🙏\n\n"
        "*Заказ #{order_id}*\nСумма: *{price} ₾*\n\n"
        "Пожалуйста, переведите средства на:\n`{requisites}`\n\n"
        "После оплаты нажмите «✅ Я оплатил(а)» или пришлите скриншот сюда 🥰"
    ),
    "ask_screenshot_again": "После перевода нажмите кнопку «✅ Я оплатил(а)» выше или отправьте скриншот подтверждения оплаты 📸",
    "reminder": (
        "Привет! Напоминаем о *заказе #{order_id}* ({price} ₾).\n"
        "Реквизиты: `{requisites}`\nОбработаем сразу после подтверждения оплаты 🙂"
    ),
    "invalid_receipt": (
        "Хм, мы ещё не видим оплату или скриншот некорректен 🤔 Пришлите, пожалуйста, чёткий скриншот оплаты для заказа #{order_id}"
    ),
    "paid_confirmed": (
        "Оплата подтверждена! ✅\n\nСпасибо за заказ, он уже в обработке и скоро будет отправлен.\n"
        "Ориентировочная доставка: 1–3 дня 🚚"
    ),
    "screenshot_received": "Получили! Проверим оплату и скоро подтвердим 🙏",
    "question_forwarded": "Спасибо, сообщение отправлено — скоро ответим 🙂",
},

"ka": {
    "choose_lang": "გთხოვთ აირჩიოთ ენა:",
    "welcome": (
        "გამარჯობა! მე ბოგდანი ვარ, Mind Root-ის შეკვეთების ბოტი 🍄\n\n"
        "დააჭირეთ პროდუქტს შესაკვეთად, ან „გაიგეთ მეტი“ დეტალებისთვის.\n"
        "🚚 უფასო მიწოდება მთელ საქართველოში ყველა შეკვეთაზე!\n"
        "💳 გადახდა საბანკო გადარიცხვით (TBC / BOG) ან კრიპტოვალუტით (USDT).\n\nსასიამოვნო შოპინგს გისურვებთ!"
    ),
    "name": {"mane": "Lion's Mane", "cord": "Cordyceps", "bundle": "Dual Complex (Lion's Mane + Cordyceps)"},
    "tagline": {
        "mane": "მეხსიერება / ფოკუსი / ნერვების მხარდაჭერა",
        "cord": "ენერგია / გამძლეობა / სასიცოცხლო ძალა",
        "bundle": "სრული ყოველდღიური რიტუალი — ორივე პროდუქტი (−20%)",
    },
    "learn_more_btn": "ℹ️ გაიგეთ მეტი",
    "order_btn": "🛒 შეკვეთა",
    "back_btn": "⬅️ უკან",
    "i_paid_btn": "✅ გადავიხადე",
    "pay_btn_bank": "💳 საბანკო გადარიცხვა (TBC / BOG — ₾)",
    "pay_btn_crypto": "💎 კრიპტო (USDT TRC20 / BEP20)",
    "details": {
        "mane": (
            "🧠 *Lion's Mane Mushroom*\n\n"
            "Lion's Mane (Hericium erinaceus) — ფუნქციური სოკო, რომელიც ტრადიციულად გამოიყენება "
            "გონებრივი სიცხადის, ფოკუსისა და ნერვული სისტემის მხარდასაჭერად.\n\n"
            "*შემადგენლობა:* Lion's Mane ექსტრაქტი 10:1 (Fruiting Body), 1000 მგ ულუფაზე (2 კაფსულა)\n"
            "*სხვა ინგრედიენტები:* მცენარეული ცელულოზა (კაფსულა), ბრინჯის ფქვილი, მაგნიუმის სტეარატი\n"
            "*რეკომენდებული მიღება:* 2 კაფსულა, დღეში 1–2-ჯერ, სასურველია საკვებთან ერთად\n"
            "*120 კაფსულა ქილაში — დაახლ. 2 თვის მარაგი*\n\n"
            "*გაფრთხილება:* არ გადააჭარბოთ რეკომენდებულ დოზას. კვებითი დანამატი, არ არის წამალი.\n\n"
            "*ფასი: 80 ₾*"
        ),
        "cord": (
            "⚡ *Cordyceps Mushroom*\n\n"
            "Cordyceps — ტრადიციული ფუნქციური სოკო, რომელიც გამოიყენება ენერგიის, გამძლეობისა და "
            "საერთო სასიცოცხლო ტონუსის მხარდასაჭერად.\n\n"
            "*შემადგენლობა:* Cordyceps ექსტრაქტი 8:1 (Fruiting Body, Cordyceps militaris), 1000 მგ ულუფაზე (2 კაფსულა)\n"
            "*სხვა ინგრედიენტები:* მცენარეული ცელულოზა (კაფსულა), ბრინჯის ფქვილი, მაგნიუმის სტეარატი\n"
            "*რეკომენდებული მიღება:* 2 კაფსულა, დღეში 1–2-ჯერ, სასურველია საკვებთან ერთად\n"
            "*120 კაფსულა ქილაში — დაახლ. 2 თვის მარაგი*\n\n"
            "*გაფრთხილება:* არ გადააჭარბოთ რეკომენდებულ დოზას. კვებითი დანამატი, არ არის წამალი.\n\n"
            "*ფასი: 80 ₾*"
        ),
        "bundle": (
            "🍄 *Dual Complex (Lion's Mane + Cordyceps)*\n\n"
            "ორივე პროდუქტი ერთ შეკვეთაში — 20% ფასდაკლება.\n\n"
            "*ფასი: 128 ₾ (160 ₾-ის ნაცვლად)*"
        ),
    },
    "ask_details": (
        "მშვენიერი არჩევანია! გთხოვთ გამომიგზავნოთ *ერთ შეტყობინებაში*:\n\n"
        "📞 ტელეფონის ნომერი\n"
        "✉️ ელ. ფოსტა (სპამის გარეშე — მხოლოდ შეკვეთისა და ამანათის შესახებ დასაკავშირებლად)\n"
        "🏙 ქალაქი\n"
        "🏠 მიწოდების მისამართი\n"
        "🧾 სახელი და გვარი\n\n"
        "მაგალითად:\n+995 555 123456\nname@example.com\nბათუმი\nხიმშიაშვილის ქ. 12\nგიორგი გიორგაძე"
    ),
    "choose_payment": (
        "მადლობა! თქვენი შეკვეთა *#{order_id}* მზადაა 🙏\n"
        "ჯამი: *{price} ₾*\n\n"
        "გთხოვთ აირჩიოთ გადახდის მეთოდი ქვემოთ:"
    ),
    "bank_instructions": (
        "💳 *საბანკო გადარიცხვა (TBC / BOG) — შეკვეთა #{order_id}*\n"
        "თანხა: *{price} ₾*\n\n"
        "რეკვიზიტები:\n`{requisites}`\n\n"
        "გადარიცხვის შემდეგ დააჭირეთ ღილაკს *„✅ გადავიხადე“* ქვემოთ (ან გამოგვიგზავნეთ ქვითრის სქრინშოთი აქ) 🥰"
    ),
    "crypto_instructions": (
        "💎 *კრიპტო გადახდა (USDT) — შეკვეთა #{order_id}*\n"
        "თანხა: *~{usdt} USDT* ({price} ₾)\n\n"
        "*USDT (BEP20 — BNB Smart Chain):*\n`{bep20}`\n\n"
        "*USDT (TRC20 — TRON):*\n`{trc20}`\n\n"
        "დააჭირეთ მისამართს დასაკოპირებლად. გადარიცხვის შემდეგ დააჭირეთ *„✅ გადავიხადე“* ქვემოთ (ან გამოგვიგზავნეთ სქრინშოთი) 🥰"
    ),
    "order_created": (
        "მადლობა შეკვეთისთვის! 🙏\n\n"
        "*შეკვეთა #{order_id}*\nჯამი: *{price} ₾*\n\n"
        "გთხოვთ გადარიცხოთ თანხა:\n`{requisites}`\n\n"
        "გადახდის შემდეგ დააჭირეთ „✅ გადავიხადე“ ან გამომიგზავნეთ სქრინშოთი 🥰"
    ),
    "ask_screenshot_again": "გადარიცხვის შემდეგ დააჭირეთ ღილაკს „✅ გადავიხადე“ ზემოთ ან გამოგვიგზავნეთ გადახდის დამადასტურებელი სქრინშოთი 📸",
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
}