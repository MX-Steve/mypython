cat /etc/passwd | while read var
do 
	uname=${var%%:*}; 
	str=`grep $uname /etc/shadow `;
	str1=${str#*:};
	str_pass=${str1%%:*};
	echo $uname,'-->',$str_pass;  
done
