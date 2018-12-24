from urllib import request, error
url1='http://127.0.0.1/abc/'  # /var/www/html/abc/ => not found
url2='http://127.0.0.1/ban/'  # /var/www/html/ban/ ==> 700
try:
    html1=request.urlopen(url1)
except error.HTTPError as e:
    print("error:",e)

try:
    html2=request.urlopen(url2)
except error.HTTPError as e:
    print("error:",e )