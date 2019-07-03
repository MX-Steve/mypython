#!/bin/bash
FilePath=/root/shell/service/script/test.log   # 测试日志
Version=`awk '{print $7}' /etc/redhat-release` # 获取系统的版本号
Hit=20
[ -f /etc/init.d/functions ]&& source /etc/init.d/functions
if [ $UID -ne 0 ];then
   echo "请使用root用户执行脚本"
   exit 1
fi

function_ipt(){
	awk '{print $1}' $FilePath|sort|uniq -c|sort -n -k1 >/tmp/nginx_ip.log  # 从测试日志中获取ip地址，汇总 访问量和ip地址 并存入到/tmp/nginx_ip.log
	# exec < /tmp/nginx_ip.log
	# while read line
	while `cat /tmp/nginx_ip.log`
	do
	    line = 
	    Ip=`echo $line|awk '{print $2}'`
	    Count=`echo $line|awk '{print $1}'`
	    if [ `expr $Version \>=  7.0` -eq 1 ];then
		 if [ $Count -ge $Hit -a  `firewall-cmd --list-all|grep $line|wc -l` -lt 1];then
		    firewall-cmd --permanent --add-rich-rule="rule family='ipv4' source address='$Ip' reject" >/dev/null
		    res=$?
		    if [ $res -eq 0 ];then
			 firewall-cmd --reload  >/dev/null
			 action "禁止${Ip}访问" /bin/true
				 echo $Ip >>/tmp/ip_$(date +%F).log
		    else
			 action "禁止${Ip}访问" /bin/false
		    fi
		 fi
	    else
		 if [ $Count -ge $Hit -a `iptables -L -n|grep $line|wc -l` -lt 1];then
		    iptables -I INPUT -s $Ip -j DROP >/dev/null
		    res=$?
		    if [ $res -eq 0 ];then
			 action "禁止${Ip}访问" /bin/true
				 echo $Ip >>/tmp/ip_$(date +%F).log
		    else
			 action "禁止${Ip}访问" /bin/false
		    fi
		 fi
	    fi
	done
}

function_del(){
   exec </tmp/ip_$(date +%F -d "-1day").log
   while read line 
   do 
      if [ `expr $Version \>=  7.0` -eq 1 ];then
		  if [ `firewall-cmd --list-all|grep $line|wc -l`  -ge 1 ];then
			   #iptables -D INPUT -s $Ip -j DROP >/dev/null
			   firewall-cmd --permanent --remove-rich-rule 'rule service name=ssh family=ipv4 source address=192.168.1.0/24 accept' >/dev/null
			   res=$?
			   if [ $res -eq 0 ];then
			       firewall-cmd -reload >/dev/null
				   action "解禁${line}成功" /bin/true
				   echo $line >>/tmp/s1.txt
			   else
				   action "解禁${line}成功" /bin/false
			   fi
		  fi
	  else
	      if [ `iptables -L -n|grep $line|wc -l` -ge 1 ];then
		  iptables -D INPUT -s $Ip -j DROP >/dev/null
		  res=$?
			if [ $res -eq 0 ];then
				action "解禁${line}成功" /bin/true
				echo $line >>/tmp/s1.txt 
			else
				action "解禁${line}成功" /bin/false 
			fi
	      fi
	  fi    
   done  
}

functions_main(){
   flag=0
   while true
   do
   sleep 180
   ((flag++))
   ipt
   [ $flag -ge 480 ]&& del && flag=0
   done
}

main