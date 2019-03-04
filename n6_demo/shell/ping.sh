#!/bin/bash
for i in 176.4.13.{2..254}
do
  ping -w1 -c1 $i &>/dev/null
  if [ $? -eq 0 ];then
     echo "$i is up"
  fi
done
