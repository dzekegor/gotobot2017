import mysql.connector
import telebot
from time import localtime,sleep
from telebot import types
bot = telebot.TeleBot("378193841:AAHlU0XYa_sCSrWZ1CNp_8BkKX0N_X28oME")



def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None

def in_storage(unique_code):
    cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='camp')
    cursor = cnx.cursor()
    query = ("SELECT * FROM users WHERE password=%s" % unique_code)
    cursor.execute(query)
    if len(list(cursor)) > 0:
        cursor.close()
        cnx.close()
        return True
    else:
        cursor.close()
        cnx.close()
        return False

def get_username_from_storage(unique_code):
    return "ABC" if in_storage(unique_code) else None

def save_chat_id(chat_id, password):
    cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='camp')
    cursor = cnx.cursor()
    query = ("UPDATE users SET chatId = %i WHERE password = '%s'" % (chat_id, password))
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    unique_code = extract_unique_code(message.text)
    reply = "Вы ввели неправильный пароль!"
    if unique_code:
        username = get_username_from_storage(unique_code)
        if username:
            save_chat_id(message.chat.id, unique_code)
            reply = "Добро пожаловать!"
    bot.reply_to(message, reply)

@bot.message_handler(commands=['ачивки'])
def send_ach(message):
    cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='camp')
    cursor = cnx.cursor()
    s = ""
    query = ("SELECT text FROM achievements WHERE chatId=%i" % message.chat.id)
    try:
        cursor.execute(query)
        s = ""
        for i in cursor:
            s += i[0]
            s += "\n"
        s = s[:-1]
    except:
        s = "У Вас пока нет ачивок :)"
            
    bot.reply_to(message,s)
    cursor.close()
    cnx.close()
@bot.message_handler(commands=['дом'])
def send_dom(message):
    cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='camp')
    cursor = cnx.cursor()
    a = message.text.split()[1:]
    s = a[0] + " " + a[1]
    if s.upper().find('DROP') == -1:
        query = ("SELECT home FROM users WHERE name='%s'" % s)
        try:
            cursor.execute(query)
            s = ""
            for i in cursor:
                s += i[0]
                s += '\n'
            s = s[:-1]
        except:
            s = "Такого пользователя нет, или Вы неправильно ввели его имя. Надо написать имя фамилия"
    else:
        s = "mysql.connector.errors.ProgrammingError: 1146 (42S02): Table 'camp.users' doesn't exist"
        query = ("INSERT INTO gady (chatId) VALUES (%i)" % message.chat.id)
        cursor.execute(query)
        cnx.commit()
    bot.reply_to(message,s)
    cursor.close()
    cnx.close()
@bot.message_handler(commands=['телефон'])
def send_phone(message):
    cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='camp')
    cursor = cnx.cursor()
    a = message.text.split()[1:]
    s = a[0] + " " + a[1]
    if s.upper().find('DROP') == -1:
        query = ("SELECT phone FROM users WHERE name='%s'" % s)
        try:
            cursor.execute(query)
            s = ""
            for i in cursor:
                s += i[0]
                s += '\n'
            s = s[:-1]
        except:
            s = "Такого пользователя нет, или Вы неправильно ввели его имя. Надо написать имя фамилия"
    else:
        s = "mysql.connector.errors.ProgrammingError: 1146 (42S02): Table 'camp.users' doesn't exist"
        query = ("INSERT INTO gady (chatId) VALUES (%i)" % message.chat.id)
        cursor.execute(query)
        cnx.commit()
    bot.reply_to(message,s)
    cursor.close()
    cnx.close()
@bot.message_handler(commands=["расписание"])
def send_rasp(message):
    cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='camp')
    cursor = cnx.cursor()
    query = ("SELECT time,event FROM timetable")
    cursor.execute(query)
    s = ""
    for (time,event) in cursor:
        s += time
        s += " "
        s += event
        s += "\n"
    s = s[:-1]
    bot.reply_to(message,"Расписание на день")
    bot.send_message(message.chat.id,s)
    cursor.close()
    cnx.close()
@bot.message_handler(commands=['событие'])
def send_sob(message):
    cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='camp')
    cursor = cnx.cursor()
    s = localtime()[3]*100  + localtime()[4]
    query = ("SELECT time,event FROM timetable")
    cursor.execute(query)
    time1 = ""
    event1 = ""
    i = 0
    for (time,event) in cursor:
        
        if int(time[:2] + time[3:]) > s:
            if time1 != "":
                bot.send_message(message.chat.id,"С " + time1 + " идет " + event1)
            else:
                bot.reply_to(message,"Событий пока нет")
            i = 1
            break
        time1 = time
        event1 = event
    if i == 0:
        bot.send_message(message.chat.id,"С " + time1 + " идет " + event1)
    cursor.close()
    cnx.close()
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,"Ты можешь спросить меня:")
    s = "/ачивки - показать твои ачивки \n/дом <ИФ> - где живет участник \n/телефон <ИФ> - только тупой не поймет\n/расписание - расписание НА СЕГОДНЯ"
    bot.send_message(message.chat.id,s)


def save_team_id(chat_id,password):
    cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='camp')
    cursor = cnx.cursor()
    query = ("UPDATE teams SET chatId = %i WHERE password = '%s'" % (chat_id, password))
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
def team_in_storage(unique_code):
    cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='camp')
    cursor = cnx.cursor()
    query = ("SELECT * FROM teams WHERE password='%s'" % unique_code)
    cursor.execute(query)
    if len(list(cursor)) > 0:
        cursor.close()
        cnx.close()
        return True
    else:
        cursor.close()
        cnx.close()
        return False
def get_team_from_storage(unique_code):
    return "ABC" if team_in_storage(unique_code) else None

@bot.message_handler(commands=['квест'])
def quest_login(message):
    unique_code = extract_unique_code(message.text)
    reply = "Вы ввели неправильный пароль!"
    if unique_code:
        username = get_team_from_storage(unique_code)
        if username:
            save_team_id(message.chat.id, unique_code)
            reply = "Добро пожаловать в квестовый режим!"
    bot.reply_to(message, reply)
    if reply != "Вы ввели неправильный пароль!":
        question1(message)
def question1(message):
    cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='camp')
    cursor = cnx.cursor()
    query = ("SELECT id FROM teams WHERE chatId=%i" % message.chat.id)
    cursor.execute(query)
    query = ("SELECT * FROM quest WHERE teamId=%i" % list(cursor)[0])
    cursor.execute(query)
    text = list(cursor)[0][1]
    msg = bot.send_message(message.chat.id,text)
    cursor.close()
    cnx.close()
    bot.register_next_step_handler(msg,question)
def question(message):
    cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='camp')
    cursor = cnx.cursor()
    query = ("SELECT id FROM teams WHERE chatId=%i" % message.chat.id)
    cursor.execute(query)
    query = ("SELECT * FROM quest WHERE teamId=%s" % list(cursor)[0])
    cursor.execute(query)
    t = list(cursor)
    if t != []:
        answer = t[0][2]
        
        if message.text == answer:
            if len(t) != 1:
                bot.send_message(message.chat.id,"Правильно! Следующий вопрос сейчас подъедет.")
                query = ("DELETE FROM quest WHERE id=%i" % t[0][0])
                cursor.execute(query)
                cnx.commit()
                query = ("SELECT id FROM teams WHERE chatId=%i" % message.chat.id)
                cursor.execute(query)
                query = ("SELECT * FROM quest WHERE teamId=%i" % list(cursor)[0])
                cursor.execute(query)
                text = list(cursor)[0][1]
                msg = bot.send_message(message.chat.id,text)
                cursor.close()
                cnx.close()
                bot.register_next_step_handler(msg,question)
            else:
                
                bot.send_message(message.chat.id,"Ура! Вы завершили квест!")
                query = ("DELETE FROM quest WHERE id=%i" % t[0][0])
                cursor.execute(query)
                cnx.commit()
                query = ("SELECT chatId FROM admins")
                cursor.execute(query)
                t = list(cursor)
                query = ("SELECT name FROM teams WHERE chatId=%s" % message.chat.id)
                cursor.execute(query)
                name = list(cursor)[0][0]
                for i in t:
                    bot.send_message(i[0],"Команда " + name + " завершила квест.")
                cursor.close()
                cnx.close()
        else:
            cursor.close()
            cnx.close()
            msg = bot.send_message(message.chat.id,"Это - неправильный ответ. Ответьте еще раз!")
            bot.register_next_step_handler(msg,question)
bot.polling()











