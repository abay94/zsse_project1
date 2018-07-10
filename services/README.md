# Services

systemd - это набор программного обеспечения, которое обеспечивает основные строительные блоки для операционной системы Linux. Среди других функций он включает в себя systemd «System and Service Manager», систему инициализации, используемую для загрузки пользовательского пространства и управления системными процессами после загрузки. Это замена систем инициализации UNIX System V и Berkeley Software Distribution (BSD).

Одной из основных целей проекта systemd является унификация основных конфигураций Linux и поведения служб во всех дистрибутивах Linux.

В нашем проекте мы разделили на четыре группы : 
```
api-our.service
metric-our.service
flask-our.service
telegram-our.service
```
Каждый из которых запускают bash скрипты: api.sh, metric.sh, flask.sh, telegram.sh


![alt text](https://image.ibb.co/dz9su8/services.jpg)

Чтобы запустить службу systemctl, выполнив инструкции в файле устройства, используйте команду start. Если вы работаете как пользователь без полномочий root, вам придется использовать sudo, поскольку это повлияет на состояние операционной системы:
```
sudo systemctl start --_our.service
```
Чтобы остановить службу systemctl:
```
sudo systemctl stop --_our.service
```
Чтобы перезапустить службу systemctl:
```
sudo systemctl restart --_our.service
```

