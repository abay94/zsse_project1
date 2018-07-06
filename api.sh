#! /bin/bash

function get_pid {
        echo "get pid"
        PID8=$(pgrep -f 'python ./waterwash_unit_1.py')
        PID9=$(pgrep -f 'python ./waterwash_unit_2.py')
        PID10=$(pgrep -f 'python ./waterwash_unit_3.py')
        PID11=$(pgrep -f 'python ./sarimax_level_producing.py')
        PID14=$(pgrep -f 'python ./apitest_unit1.py')
        PID15=$(pgrep -f 'python ./apitest_unit2.py')
        PID16=$(pgrep -f 'python ./apitest_unit3.py')
}

function stop {
   get_pid
   if [ -z $PID8 ]; then
      echo "server is not running."
      exit 1
   else
      echo -n "Stopping server.."
      kill -9 $PID8
      sleep 1
      echo ".. Done."
   fi


   if [ -z $PID9 ]; then
      echo "server is not running."
      exit 1
   else
      echo -n "Stopping server.."
      kill -9 $PID9
      sleep 1
      echo ".. Done."
   fi

   if [ -z $PID10 ]; then
      echo "server is not running."
      exit 1
   else
      echo -n "Stopping server.."
      kill -9 $PID10
      sleep 1
      echo ".. Done."
   fi

   if [ -z $PID11 ]; then
      echo "server is not running."
      exit 1
   else
      echo -n "Stopping server.."
      kill -9 $PID11
      sleep 1
      echo ".. Done."
   fi
   if [ -z $PID14 ]; then
      echo "server is not running."
      exit 1
   else
      echo -n "Stopping server.."
      kill -9 $PID14
      sleep 1
      echo ".. Done."
   fi
   if [ -z $PID15 ]; then
      echo "server is not running."
      exit 1
   else
      echo -n "Stopping server.."
      kill -9 $PID15
      sleep 1
      echo ".. Done."
   fi
   if [ -z $PID16 ]; then
      echo "server is not running."
      exit 1
   else
      echo -n "Stopping server.."
      kill -9 $PID16
      sleep 1
      echo ".. Done."
   fi
}

function start {
   get_pid
   if [ -z $PID8 ]; then
      echo  "Starting server.."
      ./waterwash_unit_1.py &
      get_pid
      echo "Done. PID8=$PID"
   else
      echo "script "waterwash_unit_1.py" is already running, PID=$PID8"
   fi

      if [ -z $PID9 ]; then
      echo  "Starting server.."
      ./waterwash_unit_2.py &
      get_pid
      echo "Done. PID9=$PID"
   else
      echo "script "waterwash_unit_2.py" is already running, PID=$PID9"
   fi

      if [ -z $PID10 ]; then
      echo  "Starting server.."
      ./waterwash_unit_3.py &
      get_pid
      echo "Done. PID10=$PID"
   else
      echo "script "waterwash_unit_3.py" is already running, PID=$PID10"
   fi

      if [ -z $PID11 ]; then
      echo  "Starting server.."
      ./sarimax_level_producing.py &
      get_pid
      echo "Done. PID11=$PID"
   else
      echo "script "sarimax_level_producing.py" is already running, PID=$PID11"
   fi
   if [ -z $PID14 ]; then
      echo  "Starting server.."
      ./apitest_unit1.py &
      get_pid
      echo "Done. PID14=$PID"
   else
      echo "script "apitest_unit1.py" is already running, PID=$PID14"
   fi
      if [ -z $PID15 ]; then
      echo  "Starting server.."
      ./apitest_unit2.py &
      get_pid
      echo "Done. PID15=$PID"
   else
      echo "script "apitest_unit2.py" is already running, PID=$PID15"
   fi
      if [ -z $PID16 ]; then
      echo  "Starting server.."
      ./apitest_unit3.py &
      get_pid
      echo "Done. PID16=$PID"
   else
      echo "script "apitest_unit3.py" is already running, PID=$PID16"
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
      echo "script "waterwash_unit_1.py" is not running."
      exit 1
   else
      echo "script "waterwash_unit_1.py" is running, PID=$PID5"
   fi
   if [ -z  $PID ]; then
      echo "script "waterwash_unit_2.py" is not running."
      exit 1
   else
      echo "script "waterwash_unit_2.py" is running, PID=$PID6"
   fi
   if [ -z  $PID ]; then
      echo "script "waterwash_unit_3.py" is not running."
      exit 1
   else
      echo "script "waterwash_unit_3.py" is running, PID=$PID7"
   fi


   if [ -z  $PID ]; then
      echo "script "sarimax_level_producing.py" is not running."
      exit 1
   else
      echo "script "sarimax_level_producing.py" is running, PID=$PID8"
   fi


   if [ -z  $PID ]; then
      echo "script "apitest_unit1.py" is not running."
      exit 1
   else
      echo "script "apitest_unit1.py" is running, PID=$PID9"
   fi
   if [ -z  $PID ]; then
      echo "script "apitest_unit2.py" is not running."
      exit 1
   else
      echo "script "apitest_unit2.py" is running, PID=$PID10"
   fi
   if [ -z  $PID ]; then
      echo "script "apitest_unit3.py" is not running."
      exit 1
   else
      echo "script "apitest_unit3.py" is running, PID=$PID10"
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


