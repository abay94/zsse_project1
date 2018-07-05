#! /bin/bash

function get_pid {
	echo "get pid"
	PID1=$(pgrep -f 'python ./telegram_anomaly_detection.py')
	PID2=$(pgrep -f 'python ./telegram_bot_final.py')
	PID3=$(pgrep -f 'python ./anomaly_detetor_notificator.py')
}

function stop {
   get_pid
   if [ -z $PID1 ]; then
      echo "server is not running."
      exit 1
   else
      echo -n "Stopping server.."
      kill -9 $PID1
      sleep 1
      echo ".. Done."
   fi
   if [ -z $PID2 ]; then
      echo "server is not running."
      exit 1
   else
      echo -n "Stopping server.."
      kill -9 $PID2
      sleep 1
      echo ".. Done."
   fi
   if [ -z $PID3 ]; then
      echo "server is not running."
      exit 1
   else
      echo -n "Stopping server.."
      kill -9 $PID3
      sleep 1
      echo ".. Done."
   fi

}

function start {
   get_pid
   if [ -z $PID1 ]; then
      echo  "Starting server.."
      ./telegram_anomaly_detection.py &
      get_pid
      echo "Done. PID1=$PID"
   else
      echo "script "telegram_anomaly_detection.py" is already running, PID=$PID1"
   fi
   if [ -z $PID2 ]; then
      echo  "Starting server.."
      ./telegram_bot_final.py &
      get_pid
      echo "Done. PID2=$PID"
   else
      echo "script "telegram_bot_final.py" is already running, PID=$PID2"
   fi
   if [ -z $PID3 ]; then
      echo  "Starting server.."
      ./anomaly_detetor_notificator.py &
      get_pid
      echo "Done. PID3=$PID"
   else
      echo "script "anomaly_detetor_notificator.py" is already running, PID=$PID3"
   fi
}

function restart {

   echo  "Restarting server.."
   get_pid
   if [ -z $PID ]; then
      start
   else
      stop
      sleep 5
      start
   fi
}

function status {

   get_pid
   if [ -z  $PID ]; then
      echo "script "telegram_anomaly_detection.py" is not running."
      exit 1
   else
      echo "script "telegram_anomaly_detection.py" is running, PID=$PID1"
   fi
   if [ -z  $PID ]; then
      echo "script "telegram_bot_final" is not running."
      exit 1
   else
      echo "script "telegram_bot_final" is running, PID=$PID2"
   fi
   if [ -z  $PID ]; then
      echo "script "anomaly_detetor_notificator" is not running."
      exit 1
   else
      echo "script "anomaly_detetor_notificator" is running, PID=$PID3"
   fi

}

case "$1" in

   start)
      start
   ;;
   stop)
      stop
   ;;
   restart)
      restart
   ;;
   status)
      status
   ;;

   *)
      echo "Usage: $0 {start|stop|restart|status}"

esac
