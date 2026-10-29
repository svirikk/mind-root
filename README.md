# Mind Root — сайт + Telegram-боти (один сервіс на Railway)

Сайт і `POST /api/order` — на одному сервері (як у svrd-project). Замовлення з сайту одразу падає в Telegram, бази даних немає (JSON-файли на volume).

## Як усе пов'язано

```
Сайт (кошик → форма) ──POST /api/order──► web_server.py
        │  ціну й знижку рахує СЕРВЕР (pricing.py), браузеру не довіряємо
        ▼
   картка замовлення в Admin-боті «Website»   ← це і є «замовлення летить мені в Telegram»
        │
   екран підтвердження на сайті: реквізити + кнопка «Надіслати чек в Telegram»
        │  t.me/<Bogdan>?start=order_<id>_<token>
        ▼
   Bogdan прив'язує чат покупця до замовлення → скриншот падає в ту ж картку,
   кнопки ✅ Оплачено / 🔔 Нагадати / ❌ Невірний чек пишуть покупцю самі

Telegram-клієнт ─► Bogdan ─► картка в Admin-боті «Telegram»        (автоматично)
Instagram ─► ти вручну /new в Admin-боті «Instagram»               (Meta не дає API для Direct)
```

Сайт чесний щодо статусу: сторінка підтвердження каже «власника сповіщено» **лише якщо Telegram реально прийняв повідомлення** (`notified: true`). Якщо ні (немає токена / Telegram недоступний) — замовлення збережене, а покупець бачить попередження й посилання, як написати вам з номером замовлення.

## Знижка (єдине джерело істини)

80 ₾ за баночку. Від 2 баночок у кошику — 20% на **весь** кошик, один раз. `Dual Complex` = 2 баночки (1 Lion's Mane + 1 Cordyceps). Тому: 1→80, 2→128, 3→192, 4→256, Dual→128, Dual+1 баночка→192 (подвійної знижки немає).
Змінити ціну: `public/assets/js/pricing.js` **і** `pricing.py` (разом!) → `./tests/run_all.sh`.

## Підключення — покроково

**1. Боти (@BotFather)** — створи 3–4 боти й збережи токени:
| Бот | Змінна |
|---|---|
| Bogdan (покупці) | `BOT_TOKEN` (+ його username без @ → `BUYER_BOT_USERNAME`) |
| Admin Telegram | `ADMIN_TG_BOT_TOKEN` |
| Admin Website | `ADMIN_WEB_BOT_TOKEN` |
| Admin Instagram (за бажанням) | `ADMIN_IG_BOT_TOKEN` |

Свій `chat_id` дізнайся в `@userinfobot` → `ADMIN_TG_CHAT_ID`. **Натисни `/start` у кожного адмін-бота один раз** — інакше він не може написати тобі першим.

**2. GitHub** — запуш цю папку в репозиторій.

**3. Railway** — New Project → Deploy from GitHub repo. Один сервіс, команда запуску `python main.py` (є в `Procfile`).
- **Volume** → mount path `/data`. (Наскільки я знаю, volume підключається лише до одного сервісу — тому все працює в одному процесі. Перевір у документації Railway.)
- **Variables** — усе з `.env.example`: `BOT_TOKEN`, `BUYER_BOT_USERNAME`, `ADMIN_TG_BOT_TOKEN`, `ADMIN_TG_CHAT_ID`, `ADMIN_WEB_BOT_TOKEN`, `PAYMENT_REQUISITES`, `OWNER_TELEGRAM`, `DATA_DIR=/data`.
- **Settings → Networking → Generate Domain** (потім свій домен mindroot.ge: додай Custom Domain і CNAME у DNS).

**4. Тест перед запуском** — відкрий сайт, додай 2 баночки, оформи замовлення. Мають бути: картка в Admin Website з сумою 128 ₾, на сайті — «власника сповіщено» і реквізити. Натисни «Надіслати чек в Telegram» → Bogdan відповість реквізитами. Надішли скриншот → він з'явиться під карткою. Натисни ✅ → покупцю прийде підтвердження.

**5. QR на етикетці** — веди на адресу сайту (динамічний QR, щоб змінювати без передруку).

## Що заповнити вам (позначено [у дужках] на сайті)

`public/assets/js/config.js`: email, телефон, Telegram-посилання, посилання на PDF (CoA, Halal), номер партії / «придатний до».
`public/legal.html`: політика конфіденційності / умови / повернення — це чернетки; фінальний текст має переглянути грузинський юрист.
Тексти (EN / UA / KA) — `public/assets/js/i18n.js`. **Грузинський переклад — чернетка, дайте перевірити носію.**

## Структура
```
main.py                 запускає сайт + усі боти разом
web_server.py           сайт, /api/order, чесний статус notified
pricing.py / order_validation.py   ціна й валідація на сервері
buyer_bot.py            Bogdan          admin_actions.py  кнопки адмінів (Telegram + Website)
admin_bot_*.py          тонкі запуски   manual_bot_core.py  ручний Instagram
storage.py              JSON на volume  texts.py/keyboards.py  тексти й кнопки ботів
public/                 index.html, legal.html, assets/{css,js,img}
tests/                  run_all.sh — усі тести (потрібні лише node і python3)
```

## Що перевірено, а що ні
Перевірено (offline, без мережі): усі тести — таблиця знижок (JS і Python однакова), кошик (збереження, межі, зіпсований localStorage), валідація, `/api/order` (ціна на сервері, честний `notified`, екранування HTML, honeypot, ліміт запитів), паритет перекладів EN/UA/KA, наявність усіх ключів/DOM-id/зображень.
**Не перевірено:** вигляд у реальному браузері (тут немає браузера — гляньте на телефоні й десктопі, особливо пляшки й hero) і живий запуск з реальними токенами (aiogram/aiohttp тут не встановлювались; endpoint тестувався з заглушками). Якщо щось впаде, скиньте лог або скріншот.
