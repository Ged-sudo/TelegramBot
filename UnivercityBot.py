import telebot
import settings
import requests
import smtplib
from telebot import types
from telebot import TeleBot, types
import aiogram
import psycopg2




bot = telebot.TeleBot(settings.TOKENUNIV)

Button_InputInfo = "Ввести(перезаписать) свои данные"
Button_OutInfo = "Информация обо мне"

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row(Button_InputInfo, Button_OutInfo)


def Name(message):
    try:
        Strok = 0
        
        Strok = message.text.count(" ")

        if Strok == 2:
            user_id = message.from_user.id
            con = psycopg2.connect(
            database="kursach",
            user="admin",
            password="Gozime32",
            host="127.0.0.1",
            port="5433"
            )
            cur = con.cursor()
            cur.execute(
            "update students set {}='{}' where id = {}".format("name",str(message.text), message.from_user.id)
            )
            con.commit()
            send = bot.send_message(message.chat.id, "Отлично, теперь ссылку на твой аккаунт во Вконтакте:")
            bot.register_next_step_handler(send, vkID)
        else:
            send = bot.send_message(message.chat.id, "Ты допустил ошибку! Твоя запись ФИО должна выглядить так: 'Иванов Иван Иванович'")
            bot.register_next_step_handler(send, Name)

    except Exception:
        send = bot.send_message(message.chat.id, "ты допустил ошибку! введи ещё раз своё имя:")
        bot.register_next_step_handler(send, Name)


def vkID(message):
    try:
        index = 1
        #if message.text[0] == "h" and message.text[1] == "t" and message.text[2] == "t" and message.text[3] == "p" and message.text[4] == ":" and message.text[7] == "v" and message.text[8] == "k" and message.text[9] == "." and message.text[10] == "c" and message.text[11] == "o" and message.text[12] == "m":
        index = message.text.find("https://vk.com")
        if index == 0:
            con = psycopg2.connect(
            database="kursach",
            user="admin",
            password="Gozime32",
            host="127.0.0.1",
            port="5433"
            )
            cur = con.cursor()
            cur.execute(
            "update students set {}='{}' where id = {}".format("vk_acc",str(message.text), message.from_user.id)
            )
            con.commit()
            send = bot.send_message(message.chat.id, "А теперь свой номер телефона:")
            bot.register_next_step_handler(send, phone)
        else:
            send = bot.send_message(message.chat.id, "Ты допустил ошибку! вид ствоей ссылки должен быть такой:\nhttp://vk.co/id00000000")
            bot.register_next_step_handler(send, vkID)

    except Exception:
        send = bot.send_message(message.chat.id, "Nы допустил ошибку! введи ещё раз свой vk:")
        bot.register_next_step_handler(send, vkID)


def phone(message):
    try:
        s = int(message.text)

        if len(message.text) != 11:
            send = bot.send_message(message.chat.id, "Твой номер должен состоять из 11 цифр")
            bot.register_next_step_handler(send, phone)
        elif len(message.text) == 11:
            con = psycopg2.connect(
            database="kursach",
            user="admin",
            password="Gozime32",
            host="127.0.0.1",
            port="5433"
            )
            cur = con.cursor()
            cur.execute(
            "update students set {}='{}' where id = {}".format("phone",str(message.text), message.from_user.id)
            )
            con.commit()
            send = bot.send_message(message.chat.id, "Теперь номер своей группы:")
            bot.register_next_step_handler(send, IdGroop)
    except Exception:
        send = bot.send_message(message.chat.id, "Ты допустил ошибку! Введи ещё раз свой номер в формате 89111111111")
        bot.register_next_step_handler(send, phone)


def IdGroop(message):
    try:
        s = int(message.text)
        if len(message.text) != 3:
            send = bot.send_message(message.chat.id, "Hомер группы должен состоять из 3 цифр")
            bot.register_next_step_handler(send, IdGroop)
        elif len(message.text) == 3:
            con = psycopg2.connect(
            database="kursach",
            user="admin",
            password="Gozime32",
            host="127.0.0.1",
            port="5433"
            )
            cur = con.cursor()
            cur.execute(
            "update students set {}='{}' where id = {}".format("groop_id",str(message.text), message.from_user.id)
            )
            con.commit()
            send = bot.send_message(message.chat.id, "И на конец, свою почту:")
            bot.register_next_step_handler(send, email)
    except Exception:
        send = bot.send_message(message.chat.id, "Вид номера шгруппы следующий : 111\n(всего три цифры)")
        #    IdGroop(message)
        bot.register_next_step_handler(send, IdGroop)

def email(message):
    try:
        index0 = 0

        index0 = message.text.find(".ru")
        index1 = message.text.find(".com")
        index2 = message.text.find(".рф")
        index3 = message.text.find(".su")
        index4 = message.text.find(".in")
        if index0 > 0 or index1 > 0 or index2 > 0 or index3 > 0 or index4 > 0:
            con = psycopg2.connect(
            database="kursach",
            user="admin",
            password="Gozime32",
            host="127.0.0.1",
            port="5433"
            )
            cur = con.cursor()
            cur.execute(
            "update students set {}='{}' where id = {}".format("email",str(message.text), message.from_user.id)
            )
            con.commit()
            send = bot.send_message(message.chat.id, "Ваши данные успешно записаны, если необходимо, ты можешь проверить правильность их заполнения и в слушая надобности перезаписать их")
        else:
            send = bot.send_message(message.chat.id, "Вы допустили ошибку! проверьте правильность написания вашего e-mail!")
            bot.register_next_step_handler(send, email)
    except Exception:
        send = bot.send_message(message.chat.id, "Вы допустили ошибку! проверьте правильность написания вашего e-mailvgvvvvvv!")
        bot.register_next_step_handler(send, email)


@bot.message_handler(commands=["start"])
def FirstFunc(message):
    bot.send_message(message.chat.id,"Здравствуй! Выбери кнопку, наиболее подходящую тебе!", reply_markup = keyboard)
    try:
        con = psycopg2.connect(
        database="kursach",
        user="admin",
        password="Gozime32",
        host="127.0.0.1",
        port="5433"
        )
        cur = con.cursor()

        cur.execute(
        "INSERT INTO students (id) VALUES ({})".format(message.from_user.id)
        )
        con.commit()
    except Exception:
        print("Пользователь уже есть в базе данных")

@bot.message_handler(content_types=["text"])
def incommand(message):

    if (message.text == "Информация обо мне"):
        con = psycopg2.connect(
        database = "kursach",
        user = "admin",
        password = "Gozime32",
        host = "127.0.0.1",
        port = "5433"
        )

        cur = con.cursor()

        cur.execute(
        "SELECT name, phone, email, vk_acc, groop_id  from students where id={}".format(message.from_user.id)
        )
        rows = cur.fetchall()
        for row in rows:
            #print("Name =", row[0])
            #print("Phone =", row[1])
            #print("email =", row[2])
            #print("vk_acc =", row[3])
            #print("groop_id =", row[4], "\n")
            bot.send_message(message.chat.id,"Ваше имя: {}\nВаш номер телефона: {}\nВаша почта: {}\nВаша ссылка на vk: {}\nВаша группа: {} ".format(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4])))
            #bot.send_message(message.chat.id,"Ваш номер телефона: {} ".format(str(row[1])))
            #bot.send_message(message.chat.id,"Ваша почта: {} ".format(str(row[2])))
            #bot.send_message(message.chat.id,"Ваша ссылка на vk: {} ".format(str(row[3])))
            #bot.send_message(message.chat.id,"Ваша группа: {} ".format(str(row[4])))

        con.close()



    elif (message.text == "Ввести(перезаписать) свои данные"):
        send = bot.send_message(message.chat.id, "Привет! Напиши своё ФИО:")
        bot.register_next_step_handler(send, Name)



if __name__ == '__main__':
     bot.polling(none_stop=True)
