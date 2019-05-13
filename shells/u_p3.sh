#!/bin/bash
sed -n '/bash$/s/:.*//p' /etc/passwd | while read var ;do
	passwd=`sed -rn "s/$var:([^:]+).*/\1/p" /etc/shadow`
	echo "$var","$passwd"
done
