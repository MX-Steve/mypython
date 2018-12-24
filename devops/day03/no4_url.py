import webbrowser
from urllib import request

a=request.quote('你好')
url='http://www.baidu.com?wd='+a
webbrowser.open_new_tab(url)