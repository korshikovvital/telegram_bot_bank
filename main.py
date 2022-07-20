import telebot
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!'
                                      'Я Займер-бот, помогу подобрать вам отличный займ, с лучшими условиями 😇')
    markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Займы под 0%🤑')
    item2 = types.KeyboardButton('Дебетовые карты💵')
    item3 = types.KeyboardButton('Кредитные карты💰')
    item4 = types.KeyboardButton('Горячие предложения🔥')
    markup_menu.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Как я могу тебе помочь?', reply_markup=markup_menu)


@bot.message_handler(content_types=['text'])
def menu_message(message):
    if message.text == 'Займы под 0%🤑':
        markup_reply = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton('Займер', url='https://pxl.leads.su/click/9405e7c1a1eaa921f2046f86ffb00e95')
        item2 = types.InlineKeyboardButton('eкапуста',
                                           url='https://pxl.leads.su/click/c44442f89a3ca564db75276c8b87e199')
        item3 = types.InlineKeyboardButton('Cash U', url='https://pxl.leads.su/click/462b9dc4c41983b8f25b68ee7267dd6f')
        item4 = types.InlineKeyboardButton('Webbankir',
                                           url='https://pxl.leads.su/click/1208094b069442d30f8e78309eca5caa')
        item5 = types.InlineKeyboardButton('Moneyman',
                                           url='https://pxl.leads.su/click/4dc37a6ce0d3994134865da54dc607c7')
        item6 = types.InlineKeyboardButton('МигКредит',
                                           url='https://pxl.leads.su/click/662e3c963128652796f7addee66e8eea')
        item7 = types.InlineKeyboardButton('Е-заем', url='https://pxl.leads.su/click/fd70e6e7537dda886b58a5d56f0bf1e1')
        markup_reply.add(item1, item2, item3, item4, item5, item6, item7)
        bot.send_message(message.chat.id, 'Вы выбрали займы,вот лучшие', reply_markup=markup_reply)

    elif message.text == 'Дебетовые карты💵':
        markup_reply = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton('Альфа-Карта Premium',
                                           url='https://pxl.leads.su/click/733bd6878b89378aaba35d88585a7d96')
        item2 = types.InlineKeyboardButton('Альфа банк «Alfa Travel»',
                                           url='https://pxl.leads.su/click/fb95af760f319945b0a826b33174b5c3')
        item3 = types.InlineKeyboardButton('Тинькофф All Games',
                                           url='https://pxl.leads.su/click/4367a070b25a76b637fd8757070ca7a5')
        item4 = types.InlineKeyboardButton('Альфа банк - МИР',
                                           url='https://pxl.leads.su/click/8990ab69a0712416c0b8484e7cf23c9a')
        item5 = types.InlineKeyboardButton('ХоумКредит Польза',
                                           url='https://pxl.leads.su/click/0fe091d659fabe4b7ec0305efb8c41e7')

        markup_reply.add(item1, item2, item3, item4, item5)
        bot.send_message(message.chat.id, 'Вы выбрали Дебетовые карты ,вот лучшие', reply_markup=markup_reply)

    elif message.text == 'Кредитные карты💰':
        markup_reply = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton('Альфа банк - «365 дней без %»',
                                           url='https://pxl.leads.su/click/e6ccc798c1fe9e8307d6de6fd37644db')
        item2 = types.InlineKeyboardButton('Совкомбанк карта рассрочки Халва',
                                           url='https://pxl.leads.su/click/4406101b7ae937d6b0bd540031e575af')
        item3 = types.InlineKeyboardButton('Газпромбанк удобная карта',
                                           url='https://pxl.leads.su/click/d00e8e3c84b36d82d2db5bcafadf1bc1')
        item4 = types.InlineKeyboardButton('МТС банк',
                                           url='https://pxl.leads.su/click/6b77050611b7a5eafc7ded8f62e3e483')
        item5 = types.InlineKeyboardButton('Банк Открытие',
                                           url='https://pxl.leads.su/click/a47ef1b1de227e2afe28af4bdf3181ce')
        item6 = types.InlineKeyboardButton('ВТБ - Кредитная карта Возможностей',
                                           url='https://pxl.leads.su/click/208a744b668e1e55d7c1d2fa491902b4')
        item7 = types.InlineKeyboardButton('УБРиР', url='https://pxl.leads.su/click/eb07fc188928671a12a0db526cf8c014')
        item8 = types.InlineKeyboardButton('Уралсиб', url='https://pxl.leads.su/click/daa4164766aa76e19b2699cc04626901')

        markup_reply.add(item1, item2, item3, item4, item5, item6, item7, item8)
        bot.send_message(message.chat.id, 'Вы выбрали Кредитные карты ,вот лучшие', reply_markup=markup_reply)

    elif message.text == 'Горячие предложения🔥':
        markup_reply = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton('Займер', url='https://pxl.leads.su/click/9405e7c1a1eaa921f2046f86ffb00e95')
        item2 = types.InlineKeyboardButton('eкапуста',
                                           url='https://pxl.leads.su/click/c44442f89a3ca564db75276c8b87e199')
        item3 = types.InlineKeyboardButton('Cash U', url='https://pxl.leads.su/click/462b9dc4c41983b8f25b68ee7267dd6f')
        item4 = types.InlineKeyboardButton('Webbankir',
                                           url='https://pxl.leads.su/click/1208094b069442d30f8e78309eca5caa')
        item5 = types.InlineKeyboardButton('Moneyman',
                                           url='https://pxl.leads.su/click/4dc37a6ce0d3994134865da54dc607c7')
        item6 = types.InlineKeyboardButton('МигКредит',
                                           url='https://pxl.leads.su/click/662e3c963128652796f7addee66e8eea')
        item7 = types.InlineKeyboardButton('Е-заем', url='https://pxl.leads.su/click/fd70e6e7537dda886b58a5d56f0bf1e1')
        markup_reply.add(item1, item2, item3, item4, item5, item6, item7)
        bot.send_message(message.chat.id, 'Самые горячие предложения', reply_markup=markup_reply)


bot.polling()
