python框架：Django
功能强大，应用广泛
MTV:
	M:Models :模型 数据库
	V:Views  :试图（函数）
	Template :模板
1、配置虚拟环境并激活
[root@room8pc16 python]# python3 -m venv /opt/djenv
[root@room8pc16 python]# source /opt/djenv/bin/activate
2、在虚拟环境中安装django1.11.6
(djenv) [root@room8pc16 day18]# cd dj_pkgs/ ; pip install *
>>> import django
>>> django.__version__
'1.11.6'
3、创建项目
一个项目就是django实例的各种设置集合
(djenv) [root@room8pc16 day18]# django-admin startproject mysite
4、运行项目
django为了方便程序员可以看到页面效果，内建了一个简单的web服务器，纯粹用于开发环境
的测试。如果是生产环境，需要把django项目部署在apache/nginx上。
(djenv) [root@room8pc16 day18]# cd mysite/
(djenv) [root@room8pc16 mysite]# python manage.py runserver
5、访问
http://127.0.0.1:8000/
6、如果启动项目时报错，是因为没有sqlite数据库的支持，两种解决办法
(1)重新编译python3
# yum install -y sqlite-devel
# ./configure --prefix=/usr/local/
# make && make install
(2)使用mysql数据库
(djenv) [root@room8pc16 mysite]# mysql -uroot -ptedu.cn
MariaDB [(none)]> CREATE DATABASE dj1806 DEFAULT CHARSET utf8;
7、修改django配置
# vim mysite/settings.py
ALLOWED_HOSTS = '*'       # 允许全部的客户端访问
MIDDLEWARE = [            # 关闭跨站攻击的安全配置
    ... ...
    # 'django.middleware.csrf.CsrfViewMiddleware',
    ... ...
]
DATABASES = {             # 配置django使用的数据库是mysql
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj1806',
        'USER': 'root',
        'PASSWORD': 'tedu.cn',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
LANGUAGE_CODE = 'zh-hans'       # 使用中文
TIME_ZONE = 'Asia/Shanghai'     # 时区
USE_TZ = False                  # 配置django使用本地时区
8、重新运行开发环境
(djenv) [root@room8pc16 mysite]# systemctl stop httpd
(djenv) [root@room8pc16 mysite]# python manage.py runserver 0:80
0:80是0.0.0.0:80的简写
如果报以下错误：
Did you install mysqlclient or MySQL-python?
解决办法如下：
(djenv) [root@room8pc16 mysite]# pip3 install pymysql
# vim mysite/__init__.py
import pymysql
pymysql.install_as_MySQLdb()
再次运行开发环境
(djenv) [root@room8pc16 mysite]# python manage.py runserver 0:80

9、创建相关的数据库表
(djenv) [root@room8pc16 day18]# mysql -uroot -ptedu.cn
MariaDB [(none)]> use dj1806;
MariaDB [dj1806]> show tables;   # 只有一张表
(djenv) [root@room8pc16 mysite]# python manage.py migrate
MariaDB [dj1806]> show tables;    # 创建多张表
MariaDB [dj1806]> select * from auth_user;   # 没有用户
10、创建管理员帐号
(djenv) [root@room8pc16 mysite]# python manage.py createsuperuser
密码要求8位以上，满足复杂度要求，否则无法创建
MariaDB [dj1806]> select * from auth_user \G;   # 已存在管理员帐号
11、访问后台管理界面
http://192.168.4.254/admin


