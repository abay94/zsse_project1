# Related to Telegram bot part


Эта папка состоит из файлов, для обнаружение аномалий для основных параметров газовой турбины (NGP, NPT, T1, T5, Waterwash_status) по всем агрегатом и питон скрипт телеграм бота.

Все питон скрипты запускаются через командную линию (Linux distibutive, Mac OS):

``` 
./telegram.sh start
```
останавливают:
```
./telegram.sh stop
```
перезапускуют:
``` 
./telegram.sh restart 
```

### Все три команды контролируются в systemd сервисе, название которое telegram-our.service.  

Обзорная структура показана ниже:

![alt text](https://image.ibb.co/jjBD1o/telega_git.jpg)

Здесь показаны все взаимодействие между скриптами. Telegram client - это пользователь, который подписался на телеграм бот. Пользователь напрямую отправляет сообщения на сервер телеграмм, который ждет команды. Telegram bot отправляет на flask веб сервер, идентификатор пользователя, когда пользователь подписывается на telegram bot и подписывается на аномальное уведомление. Скрипты для обнаружения аномалий проверяют каждые 10 секунд, по базе данных Influxdb/OnlineClassification/unit/-----_anomaly_status независимо от того, происходит ли аномалия в одном из параметров или нет и отправляет запрос на веб-сервер flask для отправки уведомления об аномалии пользователю, если возникает аномалия.
В базу данных Influxdb/OnlineClassification/unit/----_anomaly_status записывает питон скрипт [anomaly_detection_metric.py](zsse_project1/metric/anomaly_detection_metric.py) который находится в папке metric.

### Telegram_bot_final.py
Класс telebot инкапсулирует все вызовы API в одном классе. Он предоставляет такие функции, как send_xyz (send_message, send_document и т. Д.)
Если кратко пройтись по коду, то начинаем с декларацией telebot класса. 
______________________
token = "***************************"

bot = telebot.TeleBot(token, threaded=False)
______________________

После этой декларации нам нужно зарегистрировать некоторые так называемые обработчики сообщений. Обработчики сообщений определяют фильтры, которые должны пройти сообщение. Если сообщение передает фильтр, вызывается декорированная функция и входящее сообщение передается в качестве аргумента. 
______________________
@bot.message_handler(commands=["start"])
def keyboard (message):
   cid = message.chat.id
   user_step[cid] = 1
    bot.send_message(message.chat.id, "Выберите действие",reply_markup=markup_menu_1)
______________________

В конце, функция отправляет сообщение и меню из кнопок клиенту, которые инициализированы в начале. 
______________________
markup_menu_1 = types.ReplyKeyboardMarkup(row_width=1)
btn_ks_karaozek_2 = types.KeyboardButton('КС Караозек')
btn_nazad_to_1 = types.KeyboardButton('Назад')


markup_menu_1.add(btn_statistics, btn_otchet, btn_anomalii)
______________________


