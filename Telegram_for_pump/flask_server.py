#!/home/user/anaconda3/bin/python
from influxdb import DataFrameClient
from flask import Flask, jsonify, request  # '0.12.2'
from flask import render_template
import requests
import json
from datetime import datetime, timedelta
# source ~/venvs/flaskproj/bin/activate
import numpy as np

app = Flask(__name__)

bot_token = "*********"
list_of_users_subscribed = list()
list_of_all_users = list()


# sudo docker run -it -p 9000:9000 --name tf-serve -v /home/user/Documents/tf_model/serve/:/serve/ epigramai/model-server:light --port=9000 --model_name=test --model_base_path=./serve/test
#################### find if it is subscribed for special pump notification

def unsubscribe(user, pump):
    for each in list_of_users_subscribed:
        if (each["User"] == user["User"]):
            if (each["Pump"] == pump):
                each["Status"] = 0


def subscribe(user, pump):
    for each in list_of_users_subscribed:
        if (each["User"] == user["User"]):
            if (each["Pump"] == pump):
                each["Status"] = 1
                return 0
    list_of_users_subscribed.append(user)


def unsubscribe_from_all(user):
    for each in list_of_users_subscribed:
        if (each["User"] == user["User"]):
            each["Status"] = 0


def notify_by_pump_numb(pump_numb, alarm_text):
    for user in list_of_users_subscribed:

        if (user["Pump"] == pump_numb):
            if (user["Status"] == 1):
                _ = requests.post(
                    url='https://api.telegram.org/bot{0}/{1}'.format(bot_token,
                                                                     "sendMessage"),
                    data={'chat_id': user["User"], 'text': alarm_text}).json()


##############################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###############################



@app.route('/subscirbe', methods=['POST', 'GET'])
def subscirbe_user():
    try:
        test_json1 = request.get_json()

        user_taken = json.loads(test_json1)

    except Exception as e:
        print("somth wrong")
        raise e
    print(user_taken)
    print(list_of_users_subscribed)
    subscribe(user_taken, user_taken['Pump'])

    return "done"


@app.route('/unsubscribeall', methods=['POST', 'GET'])
def unsubscribe_all():
    try:

        test_json = request.get_json()

        loaded_r = json.loads(test_json)

        # print(loaded_r)

        unsubscribe_from_all(loaded_r)
    except Exception as e:

        raise e

    return "done"


###################TELEGRAM##############################

@app.route('/notify', methods=['POST', 'GET'])
def apicall_notify(responses2=None):
    """API Call

    Pandas dataframe (sent as a payload) from API Call
    """
    try:

        test_json = request.get_json()
        d = json.loads(test_json)
        alarm_text = d["Text"]
        pump_numb = d["Pump"]



    except Exception as e:

        raise e

    notify_by_pump_numb(pump_numb, alarm_text)

    return "OK"


@app.route('/all-users', methods=['POST', 'GET'])
def all_users():
    try:
        test_json = request.get_json()
        d = json.loads(test_json)
        user = d["User"]

    except Exception as e:

        raise e
    if not user in list_of_all_users:
        list_of_all_users.append(user)

    return "OK"


@app.route('/start-telebot', methods=['POST', 'GET'])
def start_telebot():
    try:
        test_json = request.get_json()
        _ = json.loads(test_json)

    except Exception as e:

        raise e

    for k in list_of_all_users:
        _ = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(bot_token,
                                                             "sendMessage"),
            data={'chat_id': k, 'text': "Server was started. Please /start it."}).json()

    return "OK"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
