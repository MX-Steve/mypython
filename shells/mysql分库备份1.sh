#!/bin/bash
# mx-steve 18262629610
[ -f /etc/init.d/functions ] && source /etc/init.d/functions 
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
   /usr/local/mysql/bin/mysqldump -h $Ip -P 3306 -u$User -p$Passwd -S /data/3306/mysql.sock $line >/tmp/mysql/${line}_$(date +%F).sql
   res=$?
    if [ $res -eq 0 ];then
       action "备份${line}完成" /bin/true
    else
       action "备份${line}失败" /bin/false
    fi
done


