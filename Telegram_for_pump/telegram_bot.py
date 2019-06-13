#!/home/user/anaconda3/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
from influxdb import InfluxDBClient, DataFrameClient
import time
import numpy as np
import requests
import json
import datetime




token = "743441656:AAGD_e5cy3OoYYY-g1jEjkdmHunNiXeYwS8"

bot = telebot.TeleBot(token, threaded=False)

## Iniatialization of keyboard markups
markup_menu_1 = types.ReplyKeyboardMarkup(row_width=1)
markup_menu_2 = types.ReplyKeyboardMarkup(row_width=1)
markup_menu_3 = types.ReplyKeyboardMarkup(row_width=1)
# markup_menu_3_1 = types.ReplyKeyboardMarkup(row_width=1)
# markup_menu_4 = types.ReplyKeyboardMarkup(row_width=1)
# markup_menu_5 = types.ReplyKeyboardMarkup(row_width=1)
# markup_menu_5_1 = types.ReplyKeyboardMarkup(row_width=1)
markup_menu_6 = types.ReplyKeyboardMarkup(row_width=1)
markup_menu_7 = types.ReplyKeyboardMarkup(row_width=1)
markup_menu_7_1 = types.ReplyKeyboardMarkup(row_width=1)
#sdfsdfsdfasd
## Buttons
# btn_statistics = types.KeyboardButton('Cтатистика')
btn_otchet = types.KeyboardButton('Отчет')
btn_anomalii = types.KeyboardButton('Уведомление')
# btn_ks_karaozek_2 = types.KeyboardButton('КС Караозек')
btn_wgn1_2 = types.KeyboardButton('ШГН # 1')
btn_wgn2_2 = types.KeyboardButton('ШГН # 2')
btn_wgn3_2 = types.KeyboardButton('ШГН # 3')
btn_wgn4_2 = types.KeyboardButton('ШГН # 4')
btn_wgn5_2 = types.KeyboardButton('ШГН # 5')

btn_nazad_to_1 = types.KeyboardButton('Назад')
btn_nazad_to_2 = types.KeyboardButton('Назад')
# btn_nazad_to_3= types.KeyboardButton('Назад')
# btn_nazad_to_4 = types.KeyboardButton('Назад')
# btn_nazad_to_5= types.KeyboardButton('Назад')
btn_nazad_to_6 = types.KeyboardButton('Назад')
btn_nazad_to_7= types.KeyboardButton('Назад')
btn_vnachalo = types.KeyboardButton('В начало')
# btn_stancia_3 = types.KeyboardButton('Станция')
# btn_gpa1_3 = types.KeyboardButton('ГПА 1')
# btn_gpa2_3 = types.KeyboardButton('ГПА 2')
# btn_gpa3_3 = types.KeyboardButton('ГПА 3')
# btn_stancia = types.KeyboardButton('Станция')
# btn_ks_karaozek_4 = types.KeyboardButton('КС Караозек')
# btn_sutki_5 = types.KeyboardButton('Час')
# btn_nedelia_5 = types.KeyboardButton('Сутки')
# btn_mesiac_5 = types.KeyboardButton('Неделя')
# btn_god_5 = types.KeyboardButton('Месяц')
btn_da_6 = types.KeyboardButton('Да')
btn_net_6 = types.KeyboardButton('Нет')
btn_ks_karaozek_7 = types.KeyboardButton('КС Караозек')
btn_otkaz_podpisok_7_1 = types.KeyboardButton('Отказаться от всех подписок')

## Markup menu
markup_menu_1.add(btn_otchet, btn_anomalii)
markup_menu_2.add(btn_wgn1_2, btn_wgn2_2, btn_wgn3_2, btn_wgn4_2, btn_wgn5_2, btn_nazad_to_1)
markup_menu_3.add(btn_nazad_to_2, btn_vnachalo)
# markup_menu_3_1.add(btn_nazad_to_3, btn_vnachalo)
# markup_menu_4.add(btn_ks_karaozek_4, btn_nazad_to_1)
# markup_menu_5.add(btn_sutki_5, btn_nedelia_5, btn_mesiac_5, btn_god_5, btn_nazad_to_4, btn_vnachalo)
# markup_menu_5_1.add(btn_nazad_to_5, btn_vnachalo)
markup_menu_6.add(btn_da_6, btn_net_6, btn_otkaz_podpisok_7_1)
markup_menu_7.add(btn_wgn1_2, btn_wgn2_2, btn_wgn3_2, btn_wgn4_2, btn_wgn5_2, btn_nazad_to_6, btn_vnachalo)
markup_menu_7_1.add(btn_nazad_to_7, btn_vnachalo)


user_step = {}
###############################
print("Telegram bot is running!")
#bot.send_message(350191272, "Server was started. Please /start it.")
header = {'Content-Type': 'application/json',
                  'Accept': 'application/json'}
data1 = dict()
data1['Status'] = 1
data2 = json.dumps(data1)

try:
    response = requests.post(
    url='http://localhost:5000/start-telebot',
    data=json.dumps(data2), headers=header)
except:
    print('Host can not connect, which notifies all users to restart')
    pass


###############################


def get_user_step(cid):
    if cid in user_step:
        return user_step[cid]
    else:
        user_step[cid] = 1
        return




@bot.message_handler(commands=["start"])
def keyboard (message):
    cid = message.chat.id
    user_step[cid] = 1

    header = {'Content-Type': 'application/json',
              'Accept': 'application/json'}
    data3 = dict()
    data3['User'] = cid
    data3['Status'] = 1
    data4 = json.dumps(data3)
    try:
        response = requests.post(
            url='http://localhost:5000/all-users',
            data=json.dumps(data4), headers=header)
    except:
        print('Host can not connect, which adds new users at start up')
        pass

    bot.send_message(message.chat.id, "Выберите действие",reply_markup=markup_menu_1)


## Menu when user choose title from main menu
@bot.message_handler(func=lambda message:get_user_step(message.chat.id)==1)
def main_menu(message):
    cid = message.chat.id
    if message.text == "Отчет":
        user_step[cid] = 2
        bot.send_message(message.chat.id, "Выберите ШГН", reply_markup=markup_menu_2)
    elif message.text == "Уведомление":
        user_step[cid] = 6
        bot.send_message(message.chat.id,"Желаете ли Вы подписаться на уведомление аномалий?",reply_markup=markup_menu_6)




## Menu when user choose statistics
@bot.message_handler(func=lambda message:get_user_step(message.chat.id)==2)
def main_menu(message):
    cid = message.chat.id

    ## Get connect to DB
    client = InfluxDBClient('extinflux.zeinetsse.com', 8086, 'test', '12345', 'labview')
    string_name = "ow5:name_discription"
    rs5 = client.query("SELECT last(\"ow5:name_discription\"), last(\"ow5:kpi\"), last(\"ow5:state_index_text\"), last(\"ow5:availability\")  FROM labview.autogen.ow_kpi WHERE time > now() - 10m;")
    data5 = list(rs5.get_points())
    try:
        dict_data_5 = data5[0]
    except:
        dict_data_5['last']="no val"
        dict_data_5['last_1'] = "no val"
        dict_data_5['last_2'] = "no val"
        dict_data_5['last_3'] = "no val"

    rs4 = client.query(
        "SELECT last(\"ow4:name_discription\"), last(\"ow4:kpi\"), last(\"ow4:state_index_text\"), last(\"ow4:availability\")  FROM labview.autogen.ow_kpi WHERE time > now() - 10m;")
    data4 = list(rs4.get_points())
    try:
        dict_data_4 = data4[0]
    except:
        dict_data_4['last']="no val"
        dict_data_4['last_1'] = "no val"
        dict_data_4['last_2'] = "no val"
        dict_data_4['last_3'] = "no val"

    rs3 = client.query(
        "SELECT last(\"ow3:name_discription\"), last(\"ow3:kpi\"), last(\"ow3:state_index_text\"), last(\"ow3:availability\")  FROM labview.autogen.ow_kpi WHERE time > now() - 10m;")
    data3 = list(rs3.get_points())
    try:
        dict_data_3 = data3[0]
    except:
        dict_data_3['last']="no val"
        dict_data_3['last_1'] = "no val"
        dict_data_3['last_2'] = "no val"
        dict_data_3['last_3'] = "no val"


    rs2 = client.query(
        "SELECT last(\"ow2:name_discription\"), last(\"ow2:kpi\"), last(\"ow2:state_index_text\"), last(\"ow2:availability\")  FROM labview.autogen.ow_kpi WHERE time > now() - 10m;")
    data2 = list(rs5.get_points())
    try:
        dict_data_2 = data2[0]
    except:
        dict_data_2['last']="no val"
        dict_data_2['last_1'] = "no val"
        dict_data_2['last_2'] = "no val"
        dict_data_2['last_3'] = "no val"

    rs1 = client.query(
        "SELECT last(\"ow1:name_discription\"), last(\"ow1:kpi\"), last(\"ow1:state_index_text\"), last(\"ow1:availability\")  FROM labview.autogen.ow_kpi WHERE time > now() - 10m;")
    data1 = list(rs1.get_points())
    try:
        dict_data_1 = data1[0]
    except:
        dict_data_1['last']="no val"
        dict_data_1['last_1'] = "no val"
        dict_data_1['last_2'] = "no val"
        dict_data_1['last_3'] = "no val"
    #print(dict_data)


    if message.text == "ШГН # 1":
        user_step[cid] = 3
        text_1 = """
        ШГН # 1:
        - Индекс: *{}*
        - Состояние: *{}*
        - Производительность: *{}%*
        - Доступность: *{}*.
        """.format(dict_data_1['last'], dict_data_1['last_2'], round(dict_data_1['last_1'],2), dict_data_1['last_3'])
        bot.send_message(message.chat.id, text_1, parse_mode='Markdown', reply_markup=markup_menu_3)

    elif message.text == "ШГН # 2":
        user_step[cid] = 3
        text_1 = """
        ШГН # 2:
        - Индекс: *{}*
        - Состояние: *{}*
        - Производительность: *{}%*
        - Доступность: *{}*.
        """.format(dict_data_2['last'], dict_data_2['last_2'], round(dict_data_2['last_1'],2), dict_data_2['last_3'])
        bot.send_message(message.chat.id, text_1, parse_mode='Markdown', reply_markup=markup_menu_3)

    elif message.text == "ШГН # 3":
        user_step[cid] = 3
        text_1 = """
        ШГН # 3:
        - Индекс: *{}*
        - Состояние: *{}*
        - Производительность: *{}%*
        - Доступность: *{}*.
        """.format(dict_data_3['last'], dict_data_3['last_1'], round(dict_data_3['last_2'],2), dict_data_3['last_3'])
        bot.send_message(message.chat.id, text_1, parse_mode='Markdown', reply_markup=markup_menu_3)

    elif message.text == "ШГН # 4":
        user_step[cid] = 3
        text_1 = """
        ШГН # 4:
        - Индекс: *{}*
        - Состояние: *{}*
        - Производительность: *{}%*
        - Доступность: *{}*.
        """.format(dict_data_4['last'], dict_data_4['last_2'], round(dict_data_4['last_1'],2), dict_data_4['last_3'])
        bot.send_message(message.chat.id, text_1, parse_mode='Markdown', reply_markup=markup_menu_3)

    elif message.text == "ШГН # 5":
        user_step[cid] = 3
        text_1 = """
        ШГН # 5:
        - Индекс: *{}*
        - Состояние: *{}*
        - Производительность: *{}%*
        - Доступность: *{}*.
        """.format(dict_data_5['last'], dict_data_5['last_2'], round(dict_data_5['last_1'],2), dict_data_5['last_3'])
        bot.send_message(message.chat.id, text_1, parse_mode='Markdown', reply_markup=markup_menu_3)


    elif message.text == "Назад":
        user_step[cid] = 1
        bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup_menu_1)



## Menu when user choose statistics/ks karaozek
@bot.message_handler(func=lambda message:get_user_step(message.chat.id)==3)
def main_menu(message):
    cid = message.chat.id
    if message.text == "Назад":
        user_step[cid] = 2
        bot.send_message(message.chat.id, "Выберите ШГН", reply_markup=markup_menu_2)

    elif message.text == "В начало":
        user_step[cid] = 1
        bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup_menu_1)




## Menu when user choose anomalii
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 6)
def main_menu(message):
    cid = message.chat.id
    last_name = message.chat.last_name
    first_name = message.chat.first_name
    if message.text == "Да":
        user_step[cid] = 7
        text_1 = """
                Выберите ШГН
                """
        bot.send_message(message.chat.id, text_1, reply_markup=markup_menu_7)

    elif message.text == "Отказаться от всех подписок":

        header = {'Content-Type': 'application/json',

                  'Accept': 'application/json'}

        data1 = {}


        print(str(first_name) + " " + str(last_name) + " unsubscribed from anomaly")

        data1['User'] = cid
        data1['Status'] = 0
        data1['Pump'] = 0

        data2 = json.dumps(data1)

        try:
            response = requests.post(
            url='http://localhost:5000/unsubscribeall',
            data=json.dumps(data2), headers=header)

        except:
            print('Print host can not connect')
            pass

        user_step[cid] = 1
        bot.send_message(message.chat.id, "Вы отписались от всех уведомлений!", reply_markup=markup_menu_1)


    elif message.text == "Нет":
            user_step[cid] = 1
            bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup_menu_1)


## Menu when user choose anomalii/ da
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 7)
def main_menu(message):
    cid = message.chat.id
    last_name = message.chat.last_name
    first_name = message.chat.first_name



    if message.text == "ШГН # 1":

        header = {'Content-Type': 'application/json',
                  'Accept': 'application/json'}
        data3 = {}
        data3['User'] = cid
        data3['Status'] = 1
        data3['Pump'] = 1
        data4 = json.dumps(data3)
        print(str(first_name)+" "+str(last_name)+" subscribed to anomaly to pump 1")
        try:
            response = requests.post(
            url='http://localhost:5000/subscirbe',
            data=json.dumps(data4), headers=header)
        except:
            print('Host can not connect, to subscribe a user, user wants to subscribe!')
            pass
        user_step[cid] = 10
        text_1 = """
                Вы оформили подписку и будете получать уведомление по аномалиям ШГН # 1.
                """
        bot.send_message(message.chat.id, text_1, reply_markup=markup_menu_7_1)


    elif message.text == "ШГН # 2":

        header = {'Content-Type': 'application/json',
                  'Accept': 'application/json'}
        data1 = {}
        data1['User'] = cid
        data1['Status'] = 1
        data1['Pump'] = 2
        data2 = json.dumps(data1)
        print(str(first_name)+" "+str(last_name)+" subscribed to anomaly to pump 2")
        try:
            _ = requests.post(url='http://localhost:5000/subscirbe',
            data=json.dumps(data2), headers=header)
        except:
            print('Host can not connect, to subscribe a user, user wants to subscribe!')
            pass
        user_step[cid] = 10
        text_1 = """
                Вы оформили подписку и будете получать уведомление по аномалиям ШГН # 2.
                """
        bot.send_message(message.chat.id, text_1, reply_markup=markup_menu_7_1)



    elif message.text == "ШГН # 3":

        header = {'Content-Type': 'application/json',
                  'Accept': 'application/json'}
        data1 = {}
        data1['User'] = cid
        data1['Status'] = 1
        data1['Pump'] = 3
        data2 = json.dumps(data1)
        print(str(first_name) + " " + str(last_name) + " subscribed to anomaly to pump 3")
        try:
            _ = requests.post(url='http://localhost:5000/subscirbe',
                              data=json.dumps(data2), headers=header)
        except:
            print('Host can not connect, to subscribe a user, user wants to subscribe!')
            pass
        user_step[cid] = 10
        text_1 = """
                       Вы оформили подписку и будете получать уведомление по аномалиям ШГН # 3.
                       """
        bot.send_message(message.chat.id, text_1, reply_markup=markup_menu_7_1)



    elif message.text == "ШГН # 4":

        header = {'Content-Type': 'application/json',
                  'Accept': 'application/json'}
        data1 = {}
        data1['User'] = cid
        data1['Status'] = 1
        data1['Pump'] = 4
        data2 = json.dumps(data1)
        print(str(first_name) + " " + str(last_name) + " subscribed to anomaly to pump 4")
        try:
            _ = requests.post(url='http://localhost:5000/subscirbe',
                              data=json.dumps(data2), headers=header)
        except:
            print('Host can not connect, to subscribe a user, user wants to subscribe!')
            pass
        user_step[cid] = 10
        text_1 = """
                       Вы оформили подписку и будете получать уведомление по аномалиям ШГН # 4.
                       """
        bot.send_message(message.chat.id, text_1, reply_markup=markup_menu_7_1)


    elif message.text == "ШГН # 5":

        header = {'Content-Type': 'application/json',
                  'Accept': 'application/json'}
        data1 = {}
        data1['User'] = cid
        data1['Status'] = 1
        data1['Pump'] = 5
        data2 = json.dumps(data1)
        print(str(first_name) + " " + str(last_name) + " subscribed to anomaly to pump 5")
        try:
            _ = requests.post(url='http://localhost:5000/subscirbe',
                              data=json.dumps(data2), headers=header)
        except:
            print('Host can not connect, to subscribe a user, user wants to subscribe!')
            pass
        user_step[cid] = 10
        text_1 = """
                       Вы оформили подписку и будете получать уведомление по аномалиям ШГН # 5.
                       """
        bot.send_message(message.chat.id, text_1, reply_markup=markup_menu_7_1)






    elif message.text == "Назад":
        user_step[cid] = 6
        bot.send_message(message.chat.id, "Желаете ли Вы подписаться на уведомление аномалий?", reply_markup=markup_menu_6)

    elif message.text == "В начало":
        user_step[cid] = 1
        bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup_menu_1)



## Menu when user choose anomalii/ da /
@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 10)
def main_menu(message):
    cid = message.chat.id

    if message.text == "Назад":
        user_step[cid] = 6
        bot.send_message(message.chat.id, "Желаете ли Вы подписаться на уведомление аномалий?", reply_markup=markup_menu_6)

    elif message.text == "В начало":
        user_step[cid] = 1
        bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup_menu_1)



if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True, timeout = 300)
        except Exception as e:
            print(e)
            time.sleep(5)
# bot.polling(none_stop=True, interval = 0, timeout = 180)




