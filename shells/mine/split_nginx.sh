#!/bin/bash
mv /usr/local/nginx/logs/access.log /data/`date +"%Y%m%d%H"`.log
kill -USR1 `cat /usr/local/nginx/logs/nginx.pid`

# chmod +x /opt/split_nginx.sh
# crontab -e
# 0 * * * * /opt/split_nginx.sh
