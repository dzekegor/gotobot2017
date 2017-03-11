import mysql.connector
import telebot
from time import localtime,sleep

bot = telebot.TeleBot("378193841:AAHlU0XYa_sCSrWZ1CNp_8BkKX0N_X28oME")
def check(t):
    cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='camp')
    cursor = cnx.cursor()
    s = t[3]*100 + t[4]
    query = ("SELECT time,event FROM timetable")
    cursor.execute(query)
    i = 0
    for (time1,event) in cursor:
        if int(time1[:2] + time1[3:]) == s:
            event1 = event
            i = 1
            break
    if i == 1:
        query = ("SELECT chatId FROM users WHERE chatId > 0")
        cursor.execute(query)
        for i in cursor:
            bot.send_message(i[0], "Началось событие " + event1)
    cursor.close()
    cnx.close()
    sleep(60)
while 1:
    check(localtime())
