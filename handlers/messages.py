HELP_MESSAGE = (
    "🤖Этот бот-ассистент создан для помощи в организации порядка в бизнесе.🤖\n\n"
    "Вот основные шаги:\n\n"
    "1. Вы заполняете анкету с инструкциями, предоставленными ботом, чтобы"
    "зарегистрировать свою компанию👾\n"
    "2. После проверки вашей анкеты администратором Вы получите доступ в"
    "комнату, с возможностью добавления одного сотрудника, создания Общего"
    "Чек-листа а также индивидуального под сотрудника👾\n"
    "3. Получить информацию о тарифах а также произвести оплату можно, нажав"
    "кнопку “Моя подписка”👾\n\n"
    "Мы всегда готовы помочь вам на каждом этапе!👨‍💻\n"
    "Напишите модератору для получения более детальной информации"
    "✉️ {name}"
)

CREATE_COMPANY_MESSAGE = (
    "Вам необходимо заполнить профиль"
    " и после успешной модерации вы получите доступ в комнату.\n\n"
    "Давайте начнем заполнять профиль Вашей компании!\n\n"
    "Продолжая диалог с ботом и предоставляя свои личные данные, вы"
    "соглашаетесь с обработкой ваших данных в соответствии с Федеральным"
    "законом 'О персональных данных' от 27.07.2006 № 152-ФЗ."
)

ENTER_IN_COMPANY_MESSAGE = (
    "Конечно, свяжитесь с администратором комнаты, чтобы он предоставил вам "
    "ID-комнаты\n\n"
    "Если он у вас уже имеется, введите его!"
)


LEAVE_ROOM_CONFIRMATION = (
    'Вы действительно хотите покинуть комнату {room_id}?\n\n'
    'Для подтверждения напишите слово "Покинуть"'
)

MODERATOR_GREETING = "Здравствуйте! Вы модератор. Вам будут высылаться заявки.\n\n" \
                     "Заявки будут Вам отправлены как только они поступят."

WELCOME_MESSAGE = "Приветствую, {name}! \n\n" \
                  "Чтобы начать взаимодействовать с ботом - " \
                  "выбери то, что тебе нужно. \n\n" \
                  "Вы также можете ознакомиться с инструкцией по работе "  \
                  "с ботом. Перейдите по ссылке https://youtu.be/vpuuiB8sbDk"
FIRE_EMPLOYEE_MESSAGE = (
    "Вы действительно хотите уволить {employee_name}?\n\n"
    "Все его данные и результаты за месяц будут удалены!\n\n"
    "Для подтверждения напишите слово 'Уволить'"
)

APPROVAL_MESSAGE_MODERATOR = "Ваша заявка прошла модерацию!\n" \
                             "Комната успешно создана!\n" \
                             "Идентификатор комнаты: {room_id}\n" \
                             "Сохраните его в надежном месте!"

REJECTION_MESSAGE_MODERATOR = (
    "К сожалению Ваша заявка отклонена модератором. \n"
    "Напишите модератору для получения более детальной информации"
    "✉️ {name}"
)

LIMIT_EMPLOYEES_MESSAGE = (
    'Пользователь {name} хочет присоединиться в вашу комнату!\n'
    'Вы не можете принять либо отклонить, так как у вас превышен лимит сотрудников!\n'
    'Вы можете улучшить подписку и попросить повторить попытку сотрудника.'
)