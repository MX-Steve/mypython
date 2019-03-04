#!/bin/bash
>hosts.txt
myping() {
  ping -W1 -c1 $1 &>/dev/null
  if [ $? -eq 0 ];then
    echo $1 >> hosts.txt
  fi
}

for i in 176.4.13.{2..254}
do
  myping $i & 
done &
