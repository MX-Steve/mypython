#!/bin/bash
#baijun 136099001@qq.com 2018-11-23
[ -f /etc/init.d/functions ]&& source /etc/init.d/functions
User="root"
Passwd="baijun123"
Sock="/data/3306/mysql.sock"
no_database="*_schema|mysql|sys|Database"
Ip="192.168.91.138"

if [  -e ${Sock} ];then
   printf "mysql is starting...\n"
else
   printf "mysql is stop...\n"
   exit 0
fi

cmd="show databases;"
/usr/local/mysql/bin/mysql -u$User -p$Passwd -S $Sock -e "${cmd}"|egrep -v "${no_database}" >/tmp/mysql/mysql_database_$(date +%F).sql
exec < /tmp/mysql/mysql_database_$(date +%F).sql
while read line
do
   echo "开始备份${line}库"
   tables=`/usr/local/mysql/bin/mysql -u$User -p$Passwd -S $Sock -e "use ${line};show tables;"|grep -v Tables_in`
   for table in ${tables[*]}
   do
      echo "开始备份${line}库的${table}"
	  /usr/local/mysql/bin/mysqldump -h $Ip -P 3306 -u$User -p$Passwd -S $Sock $line $table>/tmp/mysql/${line}_${table}_$(date +%F).sql	  
	  res=$?
      if [ $res -eq 0 ];then
         action "备份${line}库中${table}完成" /bin/true
      else
         action "备份${line}库中${table}失败" /bin/false
      fi
   done
done
