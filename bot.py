import telebot
import conf
from telebot import types
import requests
import config
import json
import os

#ИЗМЕНИТЕ ПАРАМЕТРЫ В ФАЙЛЕ CONF.PY
SERVER_ID = conf.SERVER_ID
TOKEN = conf.TOKEN
bot = telebot.TeleBot(conf.BOT_TOKEN)

headers = {
    'Authorization': f"Bearer {TOKEN}",
    'Content-Type': 'application/json',
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Включить сервер")
    btn2 = types.KeyboardButton("Перезагрузить сервер")
    btn3 = types.KeyboardButton("Выключить сервер")
    btn4 = types.KeyboardButton("Статус сервера")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Включить сервер"):
        response = requests.post(f"https://api.cloudvps.reg.ru/v1/reglets/{SERVER_ID}/actions", headers=headers, json={'type': 'start',})
        bot.send_message(message.chat.id, "Включается!")

    elif(message.text == "Выключить сервер"):
        response = requests.post(f"https://api.cloudvps.reg.ru/v1/reglets/{SERVER_ID}/actions", headers=headers, json={'type': 'stop',})
        bot.send_message(message.chat.id, "Выключается!")

    elif(message.text == "Перезагрузить сервер"):
        response = requests.post(f"https://api.cloudvps.reg.ru/v1/reglets/{SERVER_ID}/actions", headers=headers, json={'type': 'reboot',})
        bot.send_message(message.chat.id, "Перезагружается")

    elif(message.text == "Статус сервера"):
        response = requests.get('https://api.cloudvps.reg.ru/v1/balance_data', headers=headers)
        res2 = requests.get(f"https://api.cloudvps.reg.ru/v1/reglets/{SERVER_ID}", headers=headers)
        pr = json.loads(response.text)
        pr2 = json.loads(res2.text)
        if (pr['balance_data']['detalization'][0]['state'] == "stopped"): state = "Остановлен"
        else: state = "Работает"
        text = f"**Статус cервера {pr['balance_data']['detalization'][0]['name']}**:\nТарифный план: `{pr['balance_data']['detalization'][0]['plan_name']}`\nСостоянине: **{state}**\nСтоимость в месяц: **{pr['balance_data']['detalization'][0]['price_month']}**\nМой баланс: **{pr['balance_data']['balance']}**\nДней прошло: **{pr['balance_data']['days_left']}**\nЗанято места на диске: **{pr2['reglet']['disk_usage']}** из **{pr2['reglet']['disk']} Gb**\nОперативная память: **{pr2['reglet']['memory']} Mb**\nIP адрес: `{pr2['reglet']['ip']}`\nОперационная система: **{pr2['reglet']['image']['name']}**\n**{pr2['reglet']['hostname']}**"
        bot.send_message(message.chat.id, text, parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")

bot.polling(none_stop=True)