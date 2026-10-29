/* Mind Root — site copy (EN default, UA, KA). Edit freely.
   Rules followed: wording stays close to the real label; no disease claims; no certifications or lab
   results beyond the documents the owner actually holds. The Georgian text is a draft — have a native
   speaker review it before launch. */
window.I18N = {
  langs: ["en", "uk", "ka"],
  labels: { en: "EN", uk: "UA", ka: "KA" },
  dict: {

/* ============================== ENGLISH ============================== */
en: {
  meta_title: "Mind Root — Functional mushroom supplements, Georgia",
  meta_desc: "Lion's Mane and Cordyceps extract capsules, 120 per bottle. Transparent labels, quality documents on request, delivery across Georgia.",
  skip: "Skip to content",
  nav_products: "Products", nav_about: "About", nav_how: "How to order", nav_faq: "FAQ",
  cart_open: "Open cart", menu: "Menu", lang_label: "Language",

  hero_title: "Nature. <em>In Your Daily Rhythm.</em>",
  hero_sub: "Discover functional mushrooms for your everyday routine.",
  hero_cta1: "Explore Products", hero_cta2: "Discover Mind Root",
  trust1: "Transparent ingredients", trust2: "Quality documents on request", trust3: "Delivery across Georgia",
  hero_tag: "Dual Complex — both bottles, <b>128 ₾</b>",

  prod_title: "Two extracts. One simple routine.",
  prod_sub: "Each bottle holds 120 capsules. Add two or more bottles and 20% comes off automatically.",
  per_bottle: "per bottle", add_to_cart: "Add to cart", learn_more: "Learn more", qty: "Quantity",
  bundle_badge: "Bundle · −20%", was: "was",
  mane_desc: "Hericium erinaceus fruiting-body extract (10:1). A functional mushroom traditionally valued for focus and mental clarity.",
  cord_desc: "Cordyceps militaris fruiting-body extract (8:1). A traditional functional mushroom valued for energy and stamina.",
  dual_name: "Dual Complex",
  dual_desc: "One Lion's Mane and one Cordyceps bottle, together. The same two products as above, sold as a set.",
  bundle_note: "Counts as two bottles. The 20% is applied once, never twice.",

  d_title: "Product details",
  d_inside: "What's inside", d_serving: "Serving information", d_docs: "Quality documents", d_storage: "Storage",
  d_extract: "Active ingredient", d_amount: "Per serving", d_other: "Other ingredients", d_origin: "Origin",
  d_capsules: "Capsules per bottle", d_servings: "Servings per bottle", d_size: "Serving size", d_use: "Suggested use (from the label)",
  d_coa: "Manufacturer's Certificate of Analysis (extract)", d_halal: "Manufacturer's Halal certificate",
  d_batch: "Batch / best-before", d_open: "Open PDF", d_request: "available on request",
  d_faq: "Good to know",
  d_delivery: "Delivery across Georgia is free and usually takes 1–3 days after payment is confirmed.",
  d_disclaimer: "This product is a dietary supplement and is not intended to diagnose, treat, cure or prevent any disease. Do not exceed the recommended dose. Pregnant or nursing women, children under 18, and people with a medical condition or taking medication should consult a healthcare professional before use.",
  mane_lead: "Lion's Mane (Hericium erinaceus) is a functional mushroom traditionally valued for its potential to support cognitive health, focus and nerve function. Mind Root Lion's Mane is a 10:1 extract made from the fruiting body.",
  cord_lead: "Cordyceps is a traditional functional mushroom valued for its potential to support energy, stamina and overall vitality. Mind Root Cordyceps is an 8:1 extract of Cordyceps militaris, made from the fruiting body.",
  dual_lead: "Dual Complex is simply one bottle of Lion's Mane and one bottle of Cordyceps, sold together at 128 ₾ instead of 160 ₾. It is not a third formula — the bottles are identical to the ones sold separately.",
  dual_inside: "Two separate bottles: 120 Lion's Mane capsules + 120 Cordyceps capsules.",
  q_med: "Is this a medicine?", a_med: "No. It is a dietary supplement. It is not intended to diagnose, treat, cure or prevent any disease.",
  q_doc: "Who should check with a doctor first?", a_doc: "Pregnant or nursing women, children under 18, and anyone with a medical condition or taking medication should consult a healthcare professional before use.",

  about_title: "Rooted in nature. Built on transparency.",
  about_p1: "Mind Root brings functional mushroom extracts to Georgia in a simple daily format: 120 capsules per bottle, two products, nothing hidden.",
  about_p2: "Every label shows exactly what is inside — the mushroom, the part used, the extract ratio and the amount per serving. We keep the manufacturer's quality documents and share them on request.",
  about_p3: "We don't promise medical results. These are dietary supplements, meant to sit alongside a balanced lifestyle.",

  how_title: "How to order",
  steps: [
    { t: "Choose products", d: "Pick Lion's Mane, Cordyceps or the Dual Complex." },
    { t: "Enter delivery details", d: "Name, phone, city and address. Telegram, WhatsApp or Instagram contact is optional." },
    { t: "Confirm payment instructions", d: "You'll see bank-transfer details right after you order. Pay and send us the receipt." },
    { t: "Receive order confirmation", d: "We confirm your payment and ship. Delivery across Georgia takes 1–3 days." }
  ],
  how_note: "Payment is by bank transfer. Delivery across Georgia is free.",

  faq_title: "Frequently asked questions",
  faq: [
    { q: "What is in each bottle?", a: "Lion's Mane: Hericium erinaceus fruiting-body extract, 10:1. Cordyceps: Cordyceps militaris fruiting-body extract, 8:1. Other ingredients: vegetable cellulose capsule, rice flour, magnesium stearate (plant source)." },
    { q: "How many capsules are in a bottle, and how long does it last?", a: "120 capsules, which is 60 servings of 2 capsules. At one serving a day a bottle lasts about two months; at two servings a day, about one month." },
    { q: "How do I take it?", a: "As printed on the label: take 2 capsules one to two times per day, preferably with a meal, or as directed by your healthcare professional. Do not exceed the recommended dose." },
    { q: "How do I pay?", a: "After you place an order you'll see bank-transfer details. Send the payment and your receipt, and we confirm the order." },
    { q: "How does delivery work?", a: "Delivery across Georgia is free and usually takes 1–3 days after we confirm your payment." },
    { q: "How will my order be confirmed?", a: "You get an order number right after submitting. We then confirm payment and shipping — on Telegram if you open our bot from the confirmation screen, or through the contact method you chose." },
    { q: "How should I store it?", a: "Store in a cool, dry place away from direct light. Keep out of reach of children." }
  ],

  cart_title: "Your order", cart_close: "Close", cart_empty: "Your cart is empty.",
  cart_subtotal: "Original subtotal", cart_discount: "Multi-bottle discount (20%)", cart_total: "Total",
  cart_hint: "Add one more bottle to get 20% off.",
  cart_free: "Delivery across Georgia: free",
  cart_checkout: "Checkout", cart_continue: "Continue shopping", cart_remove: "Remove",
  cart_bottles: "bottles", cart_set_of: "2 bottles",
  f_title: "Delivery details", f_name: "Full name", f_phone: "Phone number", f_city: "City", f_address: "Full delivery address",
  f_method: "Preferred contact (optional)", f_method_none: "No preference", f_handle: "Username or contact (optional)",
  f_consent: "I have read the {privacy} and agree that my order details are processed to fulfil my order.", f_privacy: "privacy policy",
  f_submit: "Place order", f_back: "Back to cart", f_sending: "Sending…",
  err_required: "This field is required.", err_phone: "Enter a valid phone number.", err_consent: "Please accept to continue.",
  err_generic: "We couldn't place your order. Please check the form and try again.",
  err_rate: "Too many attempts. Please wait a few minutes and try again.",
  err_network: "Connection problem. Your cart is saved — please try again.",
  done_title: "Order received", done_order: "Order",
  done_ok: "The owner has been notified. Please complete the payment below; we confirm your order once we see it.",
  done_warn_title: "Order saved, but not yet delivered to us",
  done_warn: "We couldn't notify the owner automatically. Please message us with your order number so we can confirm it.",
  done_pay: "Payment (bank transfer)", done_pay_none: "Payment details will be sent to you after we confirm the order.",
  done_tg: "Send receipt in Telegram", done_owner: "Message us on Telegram", done_ig: "Message us on Instagram",
  done_close: "Close",

  ft_tag: "Functional mushrooms for your everyday routine.",
  ft_products: "Products", ft_contact: "Contact", ft_info: "Information",
  ft_delivery: "Delivery", ft_privacy: "Privacy policy", ft_terms: "Terms", ft_returns: "Returns policy",
  ft_rights: "© Mind Root. All rights reserved.",
  ft_disclaimer: "Dietary supplements are not medicines. Statements on this site are not intended to diagnose, treat, cure or prevent any disease."
},

/* ============================== УКРАЇНСЬКА ============================== */
uk: {
  meta_title: "Mind Root — функціональні гриби, Грузія",
  meta_desc: "Капсули з екстрактом Lion's Mane та Cordyceps, по 120 у баночці. Прозорий склад, документи якості за запитом, доставка по Грузії.",
  skip: "Перейти до вмісту",
  nav_products: "Продукти", nav_about: "Про нас", nav_how: "Як замовити", nav_faq: "Питання",
  cart_open: "Відкрити кошик", menu: "Меню", lang_label: "Мова",

  hero_title: "Природа. <em>У вашому щоденному ритмі.</em>",
  hero_sub: "Функціональні гриби для вашої щоденної рутини.",
  hero_cta1: "Обрати продукти", hero_cta2: "Про Mind Root",
  trust1: "Прозорий склад", trust2: "Документи якості за запитом", trust3: "Доставка по Грузії",
  hero_tag: "Dual Complex — обидві баночки, <b>128 ₾</b>",

  prod_title: "Два екстракти. Одна проста рутина.",
  prod_sub: "У кожній баночці 120 капсул. Дві й більше баночок — знижка 20% застосовується автоматично.",
  per_bottle: "за баночку", add_to_cart: "У кошик", learn_more: "Детальніше", qty: "Кількість",
  bundle_badge: "Набір · −20%", was: "було",
  mane_desc: "Екстракт плодового тіла Hericium erinaceus (10:1). Функціональний гриб, який традиційно цінують за фокус і ясність думок.",
  cord_desc: "Екстракт плодового тіла Cordyceps militaris (8:1). Традиційний функціональний гриб, який цінують за енергію та витривалість.",
  dual_name: "Dual Complex",
  dual_desc: "Одна баночка Lion's Mane і одна Cordyceps разом. Це ті самі два продукти, що вище, — у вигляді набору.",
  bundle_note: "Рахується як дві баночки. Знижка 20% діє один раз, а не двічі.",

  d_title: "Про продукти",
  d_inside: "Склад", d_serving: "Порція", d_docs: "Документи якості", d_storage: "Зберігання",
  d_extract: "Активний інгредієнт", d_amount: "На порцію", d_other: "Інші інгредієнти", d_origin: "Походження",
  d_capsules: "Капсул у баночці", d_servings: "Порцій у баночці", d_size: "Розмір порції", d_use: "Рекомендоване застосування (з етикетки)",
  d_coa: "Сертифікат аналізу виробника (екстракт)", d_halal: "Halal-сертифікат виробника",
  d_batch: "Партія / придатний до", d_open: "Відкрити PDF", d_request: "доступно за запитом",
  d_faq: "Корисно знати",
  d_delivery: "Доставка по Грузії безкоштовна, зазвичай 1–3 дні після підтвердження оплати.",
  d_disclaimer: "Це харчова добавка, не призначена для діагностики, лікування чи профілактики захворювань. Не перевищуйте рекомендовану дозу. Вагітним, жінкам, що годують, особам до 18 років, а також за наявності захворювань чи прийому ліків слід порадитися з лікарем.",
  mane_lead: "Lion's Mane (Hericium erinaceus) — функціональний гриб, який традиційно застосовують для підтримки когнітивного здоров'я, фокусу та нервової системи. Mind Root Lion's Mane — екстракт 10:1 із плодового тіла.",
  cord_lead: "Cordyceps — традиційний функціональний гриб, який цінують за підтримку енергії, витривалості та загального тонусу. Mind Root Cordyceps — екстракт 8:1 Cordyceps militaris із плодового тіла.",
  dual_lead: "Dual Complex — це просто одна баночка Lion's Mane і одна Cordyceps за 128 ₾ замість 160 ₾. Це не третя формула: баночки такі самі, як і при окремому продажу.",
  dual_inside: "Дві окремі баночки: 120 капсул Lion's Mane + 120 капсул Cordyceps.",
  q_med: "Це ліки?", a_med: "Ні, це харчова добавка. Вона не призначена для діагностики, лікування чи профілактики захворювань.",
  q_doc: "Кому слід спершу порадитися з лікарем?", a_doc: "Вагітним, жінкам, що годують, особам до 18 років, а також тим, хто має захворювання або приймає ліки.",

  about_title: "Корені в природі. Основа — прозорість.",
  about_p1: "Mind Root привозить екстракти функціональних грибів до Грузії у простому щоденному форматі: по 120 капсул у баночці, два продукти, нічого прихованого.",
  about_p2: "На кожній етикетці видно, що саме всередині: гриб, яка частина, співвідношення екстракту та кількість на порцію. Документи якості виробника зберігаємо й показуємо за запитом.",
  about_p3: "Ми не обіцяємо медичних результатів. Це харчові добавки, які доповнюють збалансований спосіб життя.",

  how_title: "Як замовити",
  steps: [
    { t: "Оберіть продукти", d: "Lion's Mane, Cordyceps або Dual Complex." },
    { t: "Вкажіть дані доставки", d: "Ім'я, телефон, місто й адреса. Зв'язок через Telegram, WhatsApp чи Instagram — за бажанням." },
    { t: "Підтвердіть оплату", d: "Одразу після замовлення побачите реквізити для переказу. Оплатіть і надішліть чек." },
    { t: "Отримайте підтвердження", d: "Ми підтвердимо оплату й відправимо. Доставка по Грузії — 1–3 дні." }
  ],
  how_note: "Оплата — банківським переказом. Доставка по Грузії безкоштовна.",

  faq_title: "Поширені запитання",
  faq: [
    { q: "Що всередині?", a: "Lion's Mane: екстракт плодового тіла Hericium erinaceus, 10:1. Cordyceps: екстракт плодового тіла Cordyceps militaris, 8:1. Інші інгредієнти: рослинна целюлоза (капсула), рисове борошно, магнію стеарат (рослинного походження)." },
    { q: "Скільки капсул у баночці та на скільки вистачить?", a: "120 капсул — це 60 порцій по 2 капсули. По одній порції на день баночки вистачить приблизно на два місяці, по дві порції — на місяць." },
    { q: "Як приймати?", a: "Як вказано на етикетці: 2 капсули один–два рази на день, бажано під час їжі, або за рекомендацією лікаря. Не перевищуйте рекомендовану дозу." },
    { q: "Як оплатити?", a: "Після оформлення замовлення ви побачите реквізити для банківського переказу. Надішліть оплату та чек — і ми підтвердимо замовлення." },
    { q: "Як працює доставка?", a: "Доставка по Грузії безкоштовна, зазвичай 1–3 дні після підтвердження оплати." },
    { q: "Як підтверджується замовлення?", a: "Номер замовлення з'являється одразу. Далі ми підтверджуємо оплату й відправлення — у Telegram, якщо відкриєте нашого бота з екрана підтвердження, або обраним вами способом зв'язку." },
    { q: "Як зберігати?", a: "У прохолодному сухому місці, подалі від прямого світла. Зберігати в недоступному для дітей місці." }
  ],

  cart_title: "Ваше замовлення", cart_close: "Закрити", cart_empty: "Кошик порожній.",
  cart_subtotal: "Сума без знижки", cart_discount: "Знижка за кілька баночок (20%)", cart_total: "Разом",
  cart_hint: "Додайте ще одну баночку — і отримайте знижку 20%.",
  cart_free: "Доставка по Грузії: безкоштовно",
  cart_checkout: "Оформити", cart_continue: "Продовжити покупки", cart_remove: "Видалити",
  cart_bottles: "баночок", cart_set_of: "2 баночки",
  f_title: "Дані доставки", f_name: "Ім'я та прізвище", f_phone: "Номер телефону", f_city: "Місто", f_address: "Повна адреса доставки",
  f_method: "Зручний спосіб зв'язку (необов'язково)", f_method_none: "Без різниці", f_handle: "Нік або контакт (необов'язково)",
  f_consent: "Я ознайомився(лась) з {privacy} і погоджуюсь на обробку даних замовлення для його виконання.", f_privacy: "політикою конфіденційності",
  f_submit: "Підтвердити замовлення", f_back: "Назад до кошика", f_sending: "Надсилаємо…",
  err_required: "Обов'язкове поле.", err_phone: "Введіть коректний номер телефону.", err_consent: "Потрібна ваша згода.",
  err_generic: "Не вдалося оформити замовлення. Перевірте форму й спробуйте ще раз.",
  err_rate: "Забагато спроб. Зачекайте кілька хвилин.",
  err_network: "Проблема зі з'єднанням. Кошик збережено — спробуйте ще раз.",
  done_title: "Замовлення прийнято", done_order: "Замовлення",
  done_ok: "Власника сповіщено. Будь ласка, здійсніть оплату нижче; ми підтвердимо замовлення, щойно побачимо її.",
  done_warn_title: "Замовлення збережено, але нам ще не передано",
  done_warn: "Не вдалося автоматично сповістити власника. Напишіть нам із номером замовлення, і ми його підтвердимо.",
  done_pay: "Оплата (банківський переказ)", done_pay_none: "Реквізити надішлемо після підтвердження замовлення.",
  done_tg: "Надіслати чек у Telegram", done_owner: "Написати нам у Telegram", done_ig: "Написати нам в Instagram",
  done_close: "Закрити",

  ft_tag: "Функціональні гриби для вашої щоденної рутини.",
  ft_products: "Продукти", ft_contact: "Контакти", ft_info: "Інформація",
  ft_delivery: "Доставка", ft_privacy: "Політика конфіденційності", ft_terms: "Умови", ft_returns: "Повернення",
  ft_rights: "© Mind Root. Усі права захищено.",
  ft_disclaimer: "Харчові добавки не є ліками. Твердження на цьому сайті не призначені для діагностики, лікування чи профілактики захворювань."
},

/* ============================== ქართული (draft) ============================== */
ka: {
  meta_title: "Mind Root — ფუნქციური სოკოები, საქართველო",
  meta_desc: "Lion's Mane და Cordyceps ექსტრაქტის კაფსულები, 120 ცალი ქილაში. გამჭვირვალე შემადგენლობა, ხარისხის დოკუმენტები მოთხოვნით, მიწოდება მთელ საქართველოში.",
  skip: "კონტენტზე გადასვლა",
  nav_products: "პროდუქტები", nav_about: "ჩვენ შესახებ", nav_how: "როგორ შევუკვეთო", nav_faq: "კითხვები",
  cart_open: "კალათის გახსნა", menu: "მენიუ", lang_label: "ენა",

  hero_title: "ბუნება. <em>თქვენს ყოველდღიურ რიტმში.</em>",
  hero_sub: "აღმოაჩინეთ ფუნქციური სოკოები თქვენი ყოველდღიური რუტინისთვის.",
  hero_cta1: "პროდუქტების ნახვა", hero_cta2: "გაიცანით Mind Root",
  trust1: "გამჭვირვალე შემადგენლობა", trust2: "ხარისხის დოკუმენტები მოთხოვნით", trust3: "მიწოდება მთელ საქართველოში",
  hero_tag: "Dual Complex — ორივე ქილა, <b>128 ₾</b>",

  prod_title: "ორი ექსტრაქტი. ერთი მარტივი რუტინა.",
  prod_sub: "თითო ქილაში 120 კაფსულაა. ორი ან მეტი ქილის შეძენისას 20%-იანი ფასდაკლება ავტომატურად ირთვება.",
  per_bottle: "ქილა", add_to_cart: "კალათაში", learn_more: "გაიგეთ მეტი", qty: "რაოდენობა",
  bundle_badge: "კომპლექტი · −20%", was: "იყო",
  mane_desc: "Hericium erinaceus-ის ნაყოფსხეულის ექსტრაქტი (10:1). ფუნქციური სოკო, რომელიც ტრადიციულად ფასობს ფოკუსისა და გონებრივი სიცხადისთვის.",
  cord_desc: "Cordyceps militaris-ის ნაყოფსხეულის ექსტრაქტი (8:1). ტრადიციული ფუნქციური სოკო, რომელიც ფასობს ენერგიისა და გამძლეობისთვის.",
  dual_name: "Dual Complex",
  dual_desc: "ერთი Lion's Mane და ერთი Cordyceps ქილა ერთად. იგივე ორი პროდუქტი, კომპლექტად.",
  bundle_note: "ითვლება ორ ქილად. 20% გამოიყენება ერთხელ და არა ორჯერ.",

  d_title: "პროდუქტის დეტალები",
  d_inside: "შემადგენლობა", d_serving: "ულუფა", d_docs: "ხარისხის დოკუმენტები", d_storage: "შენახვა",
  d_extract: "აქტიური ინგრედიენტი", d_amount: "ულუფაზე", d_other: "სხვა ინგრედიენტები", d_origin: "წარმოშობა",
  d_capsules: "კაფსულა ქილაში", d_servings: "ულუფა ქილაში", d_size: "ულუფის ზომა", d_use: "რეკომენდებული მიღება (ეტიკეტიდან)",
  d_coa: "მწარმოებლის ანალიზის სერტიფიკატი (ექსტრაქტი)", d_halal: "მწარმოებლის Halal სერტიფიკატი",
  d_batch: "პარტია / ვარგისია", d_open: "PDF-ის გახსნა", d_request: "ხელმისაწვდომია მოთხოვნით",
  d_faq: "კარგია იცოდეთ",
  d_delivery: "მიწოდება საქართველოში უფასოა და ჩვეულებრივ 1–3 დღე სჭირდება გადახდის დადასტურების შემდეგ.",
  d_disclaimer: "ეს პროდუქტი არის კვებითი დანამატი და არ არის განკუთვნილი რაიმე დაავადების დიაგნოსტიკის, მკურნალობის ან პროფილაქტიკისთვის. არ გადააჭარბოთ რეკომენდებულ დოზას. ორსულობის, ძუძუთი კვების, 18 წლამდე ასაკის, ქრონიკული დაავადების ან მედიკამენტების მიღების შემთხვევაში მიმართეთ ექიმს.",
  mane_lead: "Lion's Mane (Hericium erinaceus) ფუნქციური სოკოა, რომელიც ტრადიციულად გამოიყენება გონებრივი ჯანმრთელობის, ფოკუსისა და ნერვული სისტემის მხარდასაჭერად. Mind Root Lion's Mane არის 10:1 ექსტრაქტი ნაყოფსხეულიდან.",
  cord_lead: "Cordyceps ტრადიციული ფუნქციური სოკოა, რომელიც ფასობს ენერგიის, გამძლეობისა და საერთო ტონუსის მხარდასაჭერად. Mind Root Cordyceps არის Cordyceps militaris-ის 8:1 ექსტრაქტი ნაყოფსხეულიდან.",
  dual_lead: "Dual Complex უბრალოდ ერთი Lion's Mane და ერთი Cordyceps ქილაა ერთად, 160 ₾-ის ნაცვლად 128 ₾-ად. ეს მესამე ფორმულა არ არის — ქილები იგივეა, რაც ცალ-ცალკე იყიდება.",
  dual_inside: "ორი ცალკე ქილა: 120 Lion's Mane კაფსულა + 120 Cordyceps კაფსულა.",
  q_med: "ეს წამალია?", a_med: "არა, ეს კვებითი დანამატია. იგი არ არის განკუთვნილი დაავადების დიაგნოსტიკის, მკურნალობის ან პროფილაქტიკისთვის.",
  q_doc: "ვინ უნდა მიმართოს ექიმს ჯერ?", a_doc: "ორსულებმა, ძუძუთი მკვებავმა დედებმა, 18 წლამდე ასაკის პირებმა, ასევე ვისაც აქვს დაავადება ან იღებს მედიკამენტებს.",

  about_title: "ბუნებაში ფესვგადგმული. გამჭვირვალობაზე აგებული.",
  about_p1: "Mind Root საქართველოში ფუნქციური სოკოების ექსტრაქტებს მარტივი ყოველდღიური ფორმატით აწვდის: 120 კაფსულა ქილაში, ორი პროდუქტი, არაფერი დამალული.",
  about_p2: "თითოეულ ეტიკეტზე ზუსტად წერია, რა არის შიგნით — სოკო, გამოყენებული ნაწილი, ექსტრაქტის თანაფარდობა და რაოდენობა ულუფაზე. მწარმოებლის ხარისხის დოკუმენტებს ვინახავთ და მოთხოვნით გიჩვენებთ.",
  about_p3: "სამედიცინო შედეგებს არ ვპირდებით. ეს კვებითი დანამატებია, რომლებიც დაბალანსებულ ცხოვრების წესს ავსებს.",

  how_title: "როგორ შევუკვეთო",
  steps: [
    { t: "აირჩიეთ პროდუქტები", d: "Lion's Mane, Cordyceps ან Dual Complex." },
    { t: "მიუთითეთ მიწოდების მონაცემები", d: "სახელი, ტელეფონი, ქალაქი და მისამართი. Telegram, WhatsApp ან Instagram კონტაქტი სურვილისამებრ." },
    { t: "დაადასტურეთ გადახდა", d: "შეკვეთისთანავე დაინახავთ საბანკო გადარიცხვის რეკვიზიტებს. გადაიხადეთ და გამოგვიგზავნეთ ჩეკი." },
    { t: "მიიღეთ დადასტურება", d: "გადახდას დავადასტურებთ და გამოვგზავნით. მიწოდება საქართველოში 1–3 დღეა." }
  ],
  how_note: "გადახდა ხდება საბანკო გადარიცხვით. მიწოდება საქართველოში უფასოა.",

  faq_title: "ხშირად დასმული კითხვები",
  faq: [
    { q: "რა არის თითო ქილაში?", a: "Lion's Mane: Hericium erinaceus-ის ნაყოფსხეულის ექსტრაქტი, 10:1. Cordyceps: Cordyceps militaris-ის ნაყოფსხეულის ექსტრაქტი, 8:1. სხვა ინგრედიენტები: მცენარეული ცელულოზის კაფსულა, ბრინჯის ფქვილი, მაგნიუმის სტეარატი (მცენარეული წარმოშობის)." },
    { q: "რამდენი კაფსულაა ქილაში და რამდენ ხანს ჰყოფნის?", a: "120 კაფსულა, ანუ 60 ულუფა თითო 2 კაფსულით. დღეში ერთი ულუფით ქილა დაახლოებით ორ თვეს ჰყოფნის, დღეში ორი ულუფით — დაახლოებით ერთ თვეს." },
    { q: "როგორ მივიღო?", a: "ეტიკეტზე მითითებულია: 2 კაფსულა დღეში ერთხელ ან ორჯერ, სასურველია საკვებთან ერთად, ან ექიმის რეკომენდაციით. არ გადააჭარბოთ რეკომენდებულ დოზას." },
    { q: "როგორ გადავიხადო?", a: "შეკვეთის შემდეგ დაინახავთ საბანკო გადარიცხვის რეკვიზიტებს. გადაიხადეთ და გამოგვიგზავნეთ ჩეკი — შეკვეთას დავადასტურებთ." },
    { q: "როგორ მუშაობს მიწოდება?", a: "მიწოდება საქართველოში უფასოა და ჩვეულებრივ 1–3 დღე სჭირდება გადახდის დადასტურების შემდეგ." },
    { q: "როგორ დადასტურდება შეკვეთა?", a: "შეკვეთის ნომერს მაშინვე იხილავთ. შემდეგ გადახდასა და გაგზავნას გიდასტურებთ — Telegram-ში, თუ დადასტურების გვერდიდან ჩვენს ბოტს გახსნით, ან თქვენ მიერ არჩეული საკონტაქტო გზით." },
    { q: "როგორ შევინახო?", a: "შეინახეთ გრილ, მშრალ ადგილას, პირდაპირი სინათლისგან მოშორებით. შეინახეთ ბავშვებისთვის მიუწვდომელ ადგილას." }
  ],

  cart_title: "თქვენი შეკვეთა", cart_close: "დახურვა", cart_empty: "კალათა ცარიელია.",
  cart_subtotal: "თავდაპირველი ჯამი", cart_discount: "ფასდაკლება რამდენიმე ქილაზე (20%)", cart_total: "სულ",
  cart_hint: "დაამატეთ კიდევ ერთი ქილა და მიიღეთ 20%-იანი ფასდაკლება.",
  cart_free: "მიწოდება საქართველოში: უფასო",
  cart_checkout: "გაფორმება", cart_continue: "შოპინგის გაგრძელება", cart_remove: "წაშლა",
  cart_bottles: "ქილა", cart_set_of: "2 ქილა",
  f_title: "მიწოდების მონაცემები", f_name: "სახელი და გვარი", f_phone: "ტელეფონის ნომერი", f_city: "ქალაქი", f_address: "მიწოდების სრული მისამართი",
  f_method: "სასურველი კონტაქტი (არასავალდებულო)", f_method_none: "არ აქვს მნიშვნელობა", f_handle: "მომხმარებლის სახელი ან კონტაქტი (არასავალდებულო)",
  f_consent: "გავეცანი {privacy}-ს და ვეთანხმები, რომ ჩემი შეკვეთის მონაცემები დამუშავდება შეკვეთის შესასრულებლად.", f_privacy: "კონფიდენციალურობის პოლიტიკას",
  f_submit: "შეკვეთის გაფორმება", f_back: "კალათაში დაბრუნება", f_sending: "იგზავნება…",
  err_required: "ველი სავალდებულოა.", err_phone: "შეიყვანეთ სწორი ტელეფონის ნომერი.", err_consent: "გაგრძელებისთვის საჭიროა თანხმობა.",
  err_generic: "შეკვეთის გაფორმება ვერ მოხერხდა. შეამოწმეთ ფორმა და სცადეთ თავიდან.",
  err_rate: "ძალიან ბევრი მცდელობა. დაელოდეთ რამდენიმე წუთს.",
  err_network: "კავშირის პრობლემა. კალათა შენახულია — სცადეთ თავიდან.",
  done_title: "შეკვეთა მიღებულია", done_order: "შეკვეთა",
  done_ok: "მფლობელს შეატყობინეს. გთხოვთ, გადაიხადოთ ქვემოთ მითითებულ რეკვიზიტებზე; გადახდის დანახვისთანავე დავადასტურებთ შეკვეთას.",
  done_warn_title: "შეკვეთა შენახულია, მაგრამ ჩვენთან ჯერ არ მოსულა",
  done_warn: "მფლობელისთვის ავტომატურად შეტყობინება ვერ გაიგზავნა. გთხოვთ, მოგვწეროთ შეკვეთის ნომრით, რომ დავადასტუროთ.",
  done_pay: "გადახდა (საბანკო გადარიცხვა)", done_pay_none: "რეკვიზიტებს გამოგიგზავნით შეკვეთის დადასტურების შემდეგ.",
  done_tg: "ჩეკის გაგზავნა Telegram-ში", done_owner: "მოგვწერეთ Telegram-ში", done_ig: "მოგვწერეთ Instagram-ზე",
  done_close: "დახურვა",

  ft_tag: "ფუნქციური სოკოები თქვენი ყოველდღიური რუტინისთვის.",
  ft_products: "პროდუქტები", ft_contact: "კონტაქტი", ft_info: "ინფორმაცია",
  ft_delivery: "მიწოდება", ft_privacy: "კონფიდენციალურობის პოლიტიკა", ft_terms: "პირობები", ft_returns: "დაბრუნების პოლიტიკა",
  ft_rights: "© Mind Root. ყველა უფლება დაცულია.",
  ft_disclaimer: "კვებითი დანამატები არ არის წამალი. ამ საიტზე მოცემული მტკიცებები არ არის განკუთვნილი დაავადების დიაგნოსტიკის, მკურნალობის ან პროფილაქტიკისთვის."
}

  }
};
