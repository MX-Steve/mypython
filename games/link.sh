#!/bin/bash
yum -y install telnet $>yum-launch.txt
if [ $? -eq 0 ]
        then
        echo "telnet功能已安装"
        else
        echo "请先配置完善yum"
fi
yum -y install expect $>>yum-launch.txt
if [ $? -eq 0 ]
        then
        echo "ecpect功能已安装"
        else
        echo "请先配置完善yum"
fi
expect << EOF
spawn telnet 176.4.200.2
expect ":" {send "tarena@mis\n"}
expect ">" {send "en\n"}
expect ":" {send "tarenamis\n"}
expect "#" {send "conf t\n"}
expect "#" {send "ip access-list extend zfy\n"}
expect "#" {send "permit ip 176.4.1`echo $num`.0 0.0.0.255 any \n"}
expect "#" {send "end\n"}
expect "#" {send "wr\n"}
expect "#" {send "exit\n"}
EOF
