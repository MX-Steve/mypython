#!/bin/bash
cat /etc/passwd | while read var;do
	uname=`echo $var | sed -r 's/([^:]+)(:.*)/\1/'`
	pass=`sed -rn 's/'$uname':([^:]+).*/\1/p' /etc/shadow`
	echo "$uname" '-->' "$pass"
done
