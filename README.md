# ML server backend of project

The whole project, we divided into five big parts which are :

```
API
FLASK
METRIC
TELEGRAM
SERVICES
```

API is dedicated to host the machine learning part of online usage of it. 
FLASK is web server that contains some one time (one request) functions and methods. 
METRIC contains python scripts that are pulls data from data base Influxdb and make calculation on them.
TELEGRAM contains all python scripts related to the telegram bot.
SERVICES contains all .service which controls whole sripts.
