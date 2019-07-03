#!/bin/bash
[ -f /etc/init.d/functions ] && source /etc/init.d/functions
if [ $UID -ne 0 ];then
   echo "请使用root用户执行脚本"
   exit 1
fi

#备份源文件
grep -rn  "sms_servers" /home/*/webjoin*/conf/server.rb_2019-02-15|awk '{print $1}'|awk -F [:] '{print $1}'|sed -r "s/(.*)/cp \1 \1_$(date +%F)/g"|bash
#获取路t径文件
grep -rn  "sms_servers" /home/*/webjoin*/conf/server.rb_2019-02-15|awk '{print $1}'|awk -F [:] '{print $1}' >> /tmp/path.txt
#获取需要替换字符
grep -rn  "sms_servers" /home/*/webjoin*/conf/server.rb_2019-02-15|awk '{print $2}'|awk -F [\"\"] '{print $2}' >> /tmp/word.txt
path=(`cat /tmp/path.txt`)
word=(`cat /tmp/word.txt`)
newword='10.181.43.24:22181'
num="${#path[*]}"
[  ${#path[*]} -ne  ${#word[*]} ]&& echo "替换内容与文件不匹配" && exit 0
for (( i=0;i<$num;i++ ))
do
    sed -i  "s/${word[$i]}/${newword}/g" ${path[$i]}
	if [ $res -eq 0 ];then
		action '替换IP成功' /bin/true
	else
		action '替换IP失败' /bin/false
	fi

     #echo "s/${word[$i]}/${newword}/g" ${path[$i]}
done

