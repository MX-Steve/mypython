#!/bin/bash
exec 9<>/dev/tcp/www.baidu.com/80

echo -ne 'GET / HTTP/1.1\r\n' >&9
echo -ne 'User-Agent: curl/7.29.0\r\n' >&9
echo -ne 'Host: www.baidu.com\r\n' >&9
echo -ne "\r\n" >&9

cat <&9
exec 9<&-
