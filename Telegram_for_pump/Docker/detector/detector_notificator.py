# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import requests

header = {'Content-Type': 'application/json', \
                  'Accept': 'application/json'}

from influxdb import InfluxDBClient
from datetime import datetime, timedelta
import time




def notifier():
    client = InfluxDBClient('extinflux.zeinetsse.com', 8086, 'test', '12345', 'labview')
    rs5 = client.query(
        "SELECT last(\"object_discription\"), last(\"messagetext\"), last(\"alerttext\"), last(\"title\")  FROM labview.autogen.events_warnings WHERE time > now() - 15s;")
    data = list(rs5.get_points())

    try:
        data5 = data[0]
        text_1 = """Уведомление!  Время: {} - Индекс: {} , {},  {},  {}. """.format(data5['time'], data5['last'], data5['last_1'], data5['last_2'], data5['last_2'])
        data1 = {}
        data1['Text'] = text_1
        data1['Pump'] = 1
        data2 = json.dumps(data1)
        _ = requests.post(url='http://flaskserver:5001/notify',
                          data=json.dumps(data2), headers=header)
    except:
        pass


    print(data)




while True:

    notifier()

    time.sleep(6)


