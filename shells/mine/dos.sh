#!/bin/bash
"这是一个针对nginx做防止dos攻击的脚本,此处要配合着日志切割实现"
FilePath=/usr/local/nginx/logs/access.log
Version=`awk '{print $4}' /etc/redhat-release | awk -F. '{print $1}'`
Hit=50
[ -f /etc/init.d/functions ]&& source /etc/init.d/functions
if [ $UID -ne 0 ];then
   echo "请使用root用户执行脚本"
   exit 1
fi

# 找出来并加入到防火墙
function_ipt(){
    awk '{print $1}' $FilePath|sort|uniq -c|sort -n -k1 >/tmp/nginx_ip.log
    cat /tmp/nginx_ip.log | while read line
    do
        Ip=`echo $line|awk '{print $2}'`
        Count=`echo $line|awk '{print $1}'`
        if [ `echo "$Version>=7.0"|bc` -eq 1 ];then
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

# 从防火墙中释放出来
function_del(){
   cat /tmp/ip_$(date +%F -d "-1day").log |  while read line 
   do 
      if [ `echo "$Version>=7.0"|bc` -eq 1 ];then
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
        let flag += 1
        function_ipt
        [ $flag -ge 480 ]&& function_del && flag=0
   done
}

functions_main
