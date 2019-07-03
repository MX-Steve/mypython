#!/bin/sh
#设置环境变量,根据java安装路径修改
export JAVA_HOME=/usr/java/jdk1.8.0_151
export JAVA_BIN=$JAVA_HOME/bin
export PATH=$PATH:$JAVA_BIN
#设置tomcat安装路径，根据安装路径修改
TomcatDir=/itworks/tomcat
StartTomcat=$TomcatDir/bin/startup.sh
TomcatCache=$TomcatDir/work

#网管系统访问地址，根据现场情况修改
WebUrl=https://26.47.30.72:8080/
TomcatMonitorLog=$TomcatDir/logs/TomcatMonitor.log
GetPageInfo=$TomcatDir/logs/TomcatMonitor.Info
Monitor()
{
 echo "[info]start monitor....`date +%Y-%m-%d,%H:%M:%S`"
 #配置tomcat全路径保证不会因为查看log等命令对该判断造成干扰，根据现场实际情况修改
 TomcatPID=`ps -ef |grep /itworks/tomcat/bin/tomcat |grep -v 'grep'|awk '{print $2}'`
 if [ "$TomcatPID" != "" ];then
    echo "[info]tomcat process ID=$TomcatPID,continue..."
    TomcatServiceCode=$(curl -k -s -o $GetPageInfo -m 10 --connect-timeout 10 $WebUrl -w %{http_code})
    if [ $TomcatServiceCode -eq 200 ];then
       echo "[info]页面返回码为$TomcatServiceCode,tomcat启动成功,测试页面正常......"
    else
       echo "[error]tomcat页面出错,请注意......状态码为$TomcatServiceCode,错误日志已输出到$GetPageInfo"
       echo "[error]页面访问出错,开始重启tomcat"
       kill $TomcatPID   # 杀掉原tomcat进程
       sleep 3
       rm -rf $TomcatCache # 清理tomcat缓存
       $StartTomcat
       sleep 300
       echo "[info]tomcat页面完成重启"
     fi
 else
     echo "[error]tomcat进程不存在!tomcat开始自动重启..."
     echo "[info]$StartTomcat,请稍候......"
     rm -rf $TomcatCache
     $StartTomcat
  fi
  echo "------------------------"
}
while true
do
  Monitor>>$TomcatMonitorLog
  sleep 60
done
