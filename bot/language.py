from pyrogram.enums import SentCodeType

CANCEL = '❌ Скасувати ❌'
CANCELED = '❌ Cкасовано'

USER_ID = '👤 Ваш user id : `{user_id}`'
SUCCESS_ADD_USER = '👤 Користувача з id {user_id} додано до білого списку'
INVALID_COMMAND_USAGE = '❌ Невірний формат команди'

THIS_COMMAND_FOR_ADMIN = '❌ Дана команда тільки для адміна'
ASK_ADMIN_ACCESS = '❌ Зверніться до адміна, щоб отримати доступ до бота'

THIS_IS_BOT = '❌ Це не аккаунт, а бот'
INVALID_ACCOUNT = '❌ Аккаунт невалідний'
ACCOUNTS_COUNT = '🧮 Кількість аккаунтів : {count}\n⭐ З преміумом : {premium}'

CHECK_PHONE = '🔎 Перевіряємо номер телефона {phone}'

BOT_FUNCTIONS = '📙 Функції бота'

BOT_COMMANDS = {
    'id': 'Повертає ваш user id',
    'menu': 'Повертає меню зі всіма функціями',
    'add_user': 'Додати користувача в білий список',
    'accounts_count': 'Кількість аккаунтів в базі'
}

FUNCTIONS = {
    'spam_to_chat': '📢 Спам в чат',
    'spam_to_comments': '📢 Спам в коментарі',
    'spam_to_pp': '📢 Спам в пп',
    'join_chats': '🚪 Доєднатися до чату / групи',
    'leave_chats': '🚪 Вийти з чату / групи',
    'reaction_raid': '👍 Рейд реакціями',
    'vote_poll': '🗳️ Голосування в опитуванні'
}

SENT_CODE_DESCRIPTION = {
    SentCodeType.APP: 'додаток Telegram',
    SentCodeType.SMS: 'SMS',
    SentCodeType.CALL: 'телефонний дзвінок',
    SentCodeType.FLASH_CALL: 'телефонний дзвінок'
}

NEW_CODE_SENT = '🔒 Новий код надіслано на {phone}'
PASSWORD_NEED = '🔑 Потрібен пароль\n__Підказка : {hint}__'
INVALID_PASSWORD = '🔑 Невірний пароль\n__Підказка : {hint}__'
INVALID_CODE = '🔒 Невірний код'
INVALID_CODE_FORMAT = '🔒 Невірний формат коду'
INVALID_PHONE = '📞 Невалідний номер телефона'
INVALID_PHONE_FORMAT = '📞 Невірний формат номера телефона'
PHONE_BANNED = '📞 Номер телефона заблоковано'
FLOOD_BAN = '❌ Тимчасовий бан за спам на {seconds} секунд'
SEND_CODE = '🔒 Відправте код\n__Код підтвердження надіслано через {by}__'
SEND_PHONE = '📞 Відправте номер телефона в форматі +380****'


SUCCESS_ADD_ACCOUNT = '''👤 Аккаунт успішно додано
🆔 ID : {user_id}
👥 Ім\'я : {first_name} {last_name}
📞 Телефон : +{phone_number}
⭐ Преміум : {is_premium}'''

ACCOUNT_ALREADY_IN_DB = '👤 Аккаунт {user_id} вже в базі даних'

NO_ACCOUNTS_IN_DB = '❌ В базі нема ні одного аккаунта'
HOW_MANY_ACCOUNTS_USE = '👥 Скільки аккаунтів використовувати?\n__Максимум {count} аккаунтів__'
PROBLEM_WITH_ACCOUNT = '❌ Проблеми з аккаунтом `{id}`'

FUNCTION_START = '✅ {text} розпочато'
SUCCESS_EMOJI = '✅'
ERROR_EMOJI = '❌'
STOPPED_EMOJI = '🛑'
STOPPED_END = 'припинено'
SUCCESS_END = 'успішно закінчено'
ERROR_END = 'не закінчено'
FUNCTION_END = '{emoji} {text} {end_text}\n__Затрачено часу {time_used}__'

TASK_NOT_FOUND = '❌ Не знайденно завдання яке потрібно відмінити'
SUCCESS_STOP_TASK = '✅ Завдання успіщно скасовано'

DEAD_STICKER = '🟥 Смертельний стікер 🟥'
ENTER_VALID_NUMBER = '👥 Введіть валідне число'
HOW_MANY_TIMES_REPEAT = '🔁 Скільки разів повідомлення з кожного аккаунта відправити?'
SPAM_BY = '⭐ Спамити за допомогою аккаунтів чи каналу?'
BY_USER = '👤 Від імені аккаунта 👤'
BY_CHANNEL = '👥 Від імені каналу 👥'
ENTER_LINK_TO_CHAT = '🔗 Введіть посилання на чат або скиньте текстовий файл з посиланнями'
INVALID_LINK_TO_CHAT = '🔗 Введіть валідне посилання на чат'
NO_ONE_LINK_TO_CHAT_IN_FILE = '📁 В файлі нема ні одного посилання на чат'
ENTER_MESSAGE = '💬 Введіть повідомлення яке потрібно надіслати або скиньте текстовий файл з повідомленнями'
EMPTY_FILE = '📁 В файлі нема повідомлень'
ENTER_TIMEOUT = '⌛ Введіть таймаут'
ENTER_LINK_TO_POST = '🔗 Введіть посилання на пост або скиньте текстовий файл з посиланнями'
INVALID_LINK_TO_POST = '🔗 Введіть валідне посилання на пост'
NO_ONE_LINK_TO_POST_IN_FILE = '📁 В файлі нема ні одного посилання на пост'
NO_ONE_NICK_NAME_IN_FILE = '📁 В файлі нема ні одного нікнейму / ID'
INVALID_NICKNAME = '🔗 Введіть валідний нікнейм / ID'
ENTER_NICKNAME_OR_ID = '🔗 Введіть нікнейм / ID або скиньте текстовий файл з нікнеймами / ID'
RANDOM_REACTION = '🎲 Рандомна реакція 🎲'
ENTER_REACTION = '👍 Яку реакцію потрібно поставити'
ENTER_LINK_TO_POST_OR_MESSAGE = '🔗 Введіть посилання на пост / повідомлення або скиньте текстовий файл з посиланнями'
INVALID_LINK_TO_POST_OR_MESSAGE = '🔗 Введіть валідне посилання на пост / повідомлення'
NO_ONE_LINK_TO_POST_OR_MESSAGE_IN_FILE = '📁 В файлі нема ні одного посилання на пост / повідомлення'
ENTER_POLL = '🗳️ Введіть за який варіант потрібно голосувати від 1 до 9'
RANDOM_POLL = '🎲 Рандомний варіант 🎲'
CANCEL_FUNCTION = '❌ Скасувати функцію'
