#!/bin/sh
#create time
#
#init
port=3306
mysql_user="root"
mysql_pwd="baijun"
CmdPath="/usr/local/mysql/bin"
mysql_sock="/data/${port}/mysql.sock"


#startmysql
function_start_mysql()
{
	if [ ! -e "$mysql_sock" ];then
	  printf "Starting MySQL ... \n"
	  mysqld --defaults-file=/data/${port}/my.cnf  2>&1 > /dev/null &
	else 
	  printf "MySQL is running...\n"
	  exit
	fi
}

#stopmysql
function_stop_mysql()
{
	if [ ! -e "$mysql_sock" ];then
	  printf "MySQL is Stopped ... \n"
	  exit
	else   
	  printf "Stop MySQL ... \n"
	    mysqladmin -u${mysql_user} -p${mysql_pwd} -S ${mysql_sock} shutdown
	fi
}


#restartmysql
function_restart_mysql()
{
	printf "Restarting	MySQL...\n"
	function_stop_mysql
	sleep 2
	function_start_mysql
}


case $1 in
start)
	function_start_mysql
;;
stop)
	function_stop_mysql
;;
restart)
	function_restart_mysql
;;
*)
   printf "Usage :/data/${port}/mysql {start|stop|restart}\n"
;;
esac
