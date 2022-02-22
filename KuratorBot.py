import telebot
import settings
import requests
import smtplib
from telebot import types
from telebot import TeleBot, types
import aiogram
import psycopg2



bot = telebot.TeleBot(settings.TOKENKUR)
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
Bin = "Вывести списки в чат"
Bout = "Вывести списки в формате .doc"
keyboard.row(Bin, Bout)



@bot.message_handler(commands=["start"])
def NOn(message):
    bot.send_message(message.chat.id, "Привет!\n Нажми на нужную кнопку пжалуйста!",  reply_markup = keyboard)

"""-------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------------------"""
def Relist(message):
    try:
        con = psycopg2.connect(
        database = "kursach",
        user = "admin",
        password = "Gozime32",
        host = "127.0.0.1",
        port = "5433"
        )
        cur = con.cursor()

        cur.execute(
        "SELECT name, phone, vk_acc from students where groop_id={}".format(message.text)
        )
        rows = cur.fetchall()
        for row in rows:
            bot.send_message(message.chat.id,"Имя студента: {} \nНомер телефона студента: {}\nСсылка на vk студента: {}".format(str(row[0]),str(row[1]),str(row[2])))
        con.commit()
    except Exception:
        send = bot.send_message(message.chat.id, "Ошибка в номере группы")
        bot.register_next_step_handler(send, Relist)


def CSV(message):
    try:
    #COPY (SELECT * FROM students where phone='01') TO 'C:/Groop.csv' CSV;
        con = psycopg2.connect(
        database = "kursach",
        user = "admin",
        password = "Gozime32",
        host = "127.0.0.1",
        port = "5433"
        )

        cur = con.cursor()

        cur.execute(
    #"set client_encoding='WIN866'"
        "COPY (SELECT * FROM students where groop_id='{}') TO 'Q:/Work/env/first/course/core/groop.pdf' CSV ".format(message.text)
        )
        con.commit()
        send = bot.send_message(message.chat.id, "Файл сформирован")
        with open("Q:/Work/env/first/course/core/groop.pdf","rb") as misc:
            file=misc.read()
        bot.send_document(message.chat.id, file)
    except Exception:
        send = bot.send_message(message.chat.id, "Ошибка в номере группы")
        bot.register_next_step_handler(send, CSV)

@bot.message_handler(content_types=["text"])
def ChatSp(message):
    if message.text == "Вывести списки в чат":
        send = bot.send_message(message.chat.id, "введи номер группы:")
        bot.register_next_step_handler(send, Relist)
    elif message.text == "Вывести списки в формате .doc":
        send = bot.send_message(message.chat.id, "Введите номер группы")
        bot.register_next_step_handler(send, CSV)
    else:
        send = bot.send_message(message.chat.id, "Я не знаю такой команды")



if __name__ == '__main__':
     bot.polling(none_stop=True)
