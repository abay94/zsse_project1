#! /bin/bash

function get_pid {
	echo "get pid"
	PID1=$(pgrep -f 'python ./unit_1.py')
	PID2=$(pgrep -f 'python ./unit_2.py')
	PID3=$(pgrep -f 'python ./unit_3.py')
	PID4=$(pgrep -f 'python ./station.py')
	PID5=$(pgrep -f 'python ./anomaly_detection_metric.py')
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
   if [ -z $PID4 ]; then
      echo "server is not running."
      exit 1
   else
      echo -n "Stopping server.."
      kill -9 $PID4
      sleep 1
      echo ".. Done."
   fi
   if [ -z $PID5 ]; then
      echo "server is not running."
      exit 1
   else
      echo -n "Stopping server.."
      kill -9 $PID5
      sleep 1
      echo ".. Done."
   fi
}

function start {
   get_pid
   if [ -z $PID1 ]; then
      echo  "Starting server.."
      ./unit_1.py &
      get_pid
      echo "Done. PID1=$PID"
   else
      echo "script "unit_1.py" is already running, PID=$PID1"
   fi
      if [ -z $PID2 ]; then
      echo  "Starting server.."
      ./unit_2.py &
      get_pid
      echo "Done. PID2=$PID"
   else
      echo "script "unit_2.py" is already running, PID=$PID2"
   fi
      if [ -z $PID3 ]; then
      echo  "Starting server.."
      ./unit_3.py &
      get_pid
      echo "Done. PID3=$PID"
   else
      echo "script "unit_3.py" is already running, PID=$PID3"
   fi
      if [ -z $PID4 ]; then
      echo  "Starting server.."
      ./station.py &
      get_pid
      echo "Done. PID4=$PID"
   else
      echo "script "station.py" is already running, PID=$PID4"
   fi
      if [ -z $PID5 ]; then
      echo  "Starting server.."
      ./anomaly_detection_metric.py &
      get_pid
      echo "Done. PID5=$PID"
   else
      echo "script "anomaly_detection_metric.py" is already running, PID=$PID5"
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
      echo "script "unit_1.py" is not running."
      exit 1
   else
      echo "script "unit_1.py" is running, PID=$PID1"
   fi
   if [ -z  $PID ]; then
      echo "script "unit_2" is not running."
      exit 1
   else
      echo "script "unit_2" is running, PID=$PID2"
   fi
   if [ -z  $PID ]; then
      echo "script "unit_3" is not running."
      exit 1
   else
      echo "script "unit_3" is running, PID=$PID3"
   fi
   if [ -z  $PID ]; then
      echo "script "station.py" is not running."
      exit 1
   else
      echo "script "station.py" is running, PID=$PID4"
   fi
   if [ -z  $PID ]; then
      echo "script "anomaly_detection_metric.py" is not running."
      exit 1
   else
      echo "script "anomaly_detection_metric.py" is running, PID=$PID5"
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
