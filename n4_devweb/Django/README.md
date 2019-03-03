<pre>

https://blog.csdn.net/qq_37489565/article/details/80612301
https://yiyibooks.cn/xx/Django_1.11.6/intro/tutorial01.html

基于python的框架
django：功能强大，应用广泛
tornado：小型框架
flask：微型框架

虚拟环境：为了保持系统的整洁与易于维护环境，采用虚拟环境，虚拟环境就是一个隔离的python
它是一个目录，激活后，安装模块都是安装到虚拟环境了。当项目结束后，清理环境只要把这个
目录删除即可

新建虚拟环境:
1、调用python的venv模块创建虚拟环境
[root@room8pc16 day03]# python3 -m venv /opt/djenv/
2、激活虚拟环境
[root@room8pc16 day03]# source /opt/djenv/bin/activate
3、退出虚拟环境
(djenv) [root@room8pc16 day03]# deactivate

安装django
(djenv) [root@room8pc16 zzg_pypkgs]# cd dj_pkgs/
(djenv) [root@room8pc16 dj_pkgs]# pip install *
(djenv) [root@room8pc16 day04]# python
>>> import django
>>> django.__version__
'1.11.6'


创建django项目
1、创建项目
(djenv) [root@room8pc16 day04]# django-admin startproject mysite
(djenv) [root@room8pc16 day04]# cd mysite/
(djenv) [root@room8pc16 mysite]# tree .
.
├── manage.py     #  用于管理项目（创建app，创建数据库、管理员）
└── mysite
    ├── __init__.py
    ├── settings.py   # 项目的配置文件
    ├── urls.py       # 路由系统URLConfig、程序入口
    └── wsgi.py       # 用于部署项目到web服务器
2、启动django自带的web服务器测试
(djenv) [root@room8pc16 mysite]# python manage.py runserver

3、配置pycharm使用虚拟环境
file -> settings -> Project day04 -> Project Interpreter -> 点右上角的齿
轮 -> add local -> 选择下面的existing，勾选make available ...，
点击右侧...，在弹出的对话框中输出/opt/djenv/bin/python

4、创建mysql数据库，用于存储django项目的数据
(djenv) [root@room8pc16 ~]# mysql -uroot -ptedu.cn
MariaDB [(none)]> create database dj1807 default charset utf8;

5、修改django配置setting.py
ALLOWED_HOSTS = '*'   # 允许所有的客户端访问
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj1807',
        'USER': 'root',
        'PASSWORD': 'tedu.cn',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False

6、配置django使用pymysql模块mysite/__init__.py
import pymysql
pymysql.install_as_MySQLdb()

7、启动测试服务器运行在所有地址的80端口
(djenv) [root@room8pc16 mysite]# python manage.py runserver 0:80

8、生成django缺省的数据库表
(djenv) [root@room8pc16 mysite]# python manage.py makemigrations
(djenv) [root@room8pc16 mysite]# python manage.py migrate

9、创建管理员帐号，密码必须8位以上，复杂
(djenv) [root@room8pc16 mysite]# python manage.py createsuperuser

10、访问后台http://127.0.0.1/admin

一个项目最好分成N多个应用，可以把不同的应用分派给不同的程序员编写
编写投票应用APP：
1、数据
两张表：
question -> 记录问题
choice -> 记录每个问题的选项，以及该选项所得的票数
2、URL：所有的投票应用，网址都以http://127.0.0.1/polls/开头
http://127.0.0.1/polls/   -> 投票首页，列出所有的问题
http://127.0.0.1/polls/1/   -> 1号问题的详情页
http://127.0.0.1/polls/1/result/  -> 1号问题投票的结果页
3、创建应用
(djenv) [root@room8pc16 mysite]# python manage.py startapp polls
4、将创建的应用注册到项目中，修改mysite/settings.py
INSTALLED_APPS = [
    ... ...
    'polls',
]
5、授权。将以http://127.0.0.1/polls/开头的URL都交给polls应用处理
修改mysite/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
]
6、在polls应用下创建urls.py
from django.conf.urls import url

urlpatterns = [
]


创建投票首页
1、创建URL，指定使用哪个视图函数进行处理
# polls/urls.py
from django.conf.urls import url
from . import views    # 使用相对导入的方式，在当前包中导入views模块

# 在http://x.x.x.x/polls/后面开始匹配
urlpatterns = [
    # 首页用views.index函数处理，为这个URL起个名字叫index
    url(r'^$', views.index, name='index'),
]
2、编写视图函数
# polls/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

3、创建模板(HTML网页)
(1) 创建polls/templates/目录
(djenv) [root@room8pc16 mysite]# mkdir polls/templates
(2) 在模板目录中创建网页
# polls/templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票首页</title>
</head>
<body>
<h1>投票首页</h1>
<hr>
<ul>
    <li>投票问题1</li>
    <li>投票问题2</li>
</ul>
</body>
</html>
4、访问http://127.0.0.1/polls/


创建投票详情页
1、配置URL
# polls/urls.py
urlpatterns = [
    ... ...
    url(r'^\d+/$', views.detail, name='detail'),
]
2、编写视图函数
# polls/views.py
def detail(request):
    return render(request, 'detail.html')
3、编写模板文件
# polls/templates/detail.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票详情页</title>
</head>
<body>
<h1>投票详情</h1>
<hr>
这是投票详情页
</body>
</html>
4、访问http://127.0.0.1/polls/数字


完善投票详情页
1、修改URL，把问题编号作为参数传递给函数
# polls/urls.py
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
2、修改视图函数，函数接受参数，并将参数传递给模板
# polls/views.py
def detail(request, question_id):
    return render(request, 'detail.html', {'question_id': question_id})
3、修改模板文件
# polls/templates/detail.html
<body>
<h1>投票详情</h1>
<hr>
这是第{{ question_id }}号问题的投票详情页
</body>


结果页
1、URL
    url(r'^(?P<question_id>\d+)/result/$', views.result, name='result'),
2、views
def result(request, question_id):
    return render(request, 'result.html', {'question_id': question_id})
3、result.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票结果页</title>
</head>
<body>
<h1>投票结果</h1>
<hr>
这是第{{ question_id }}号问题的投票结果。
</body>
</html>

创建模型Model
1、创建模型
# polls/models.py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    q = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.choice_text, self.q)

2、生成数据库中的表
(djenv) [root@room8pc16 mysite]# python manage.py makemigrations
(djenv) [root@room8pc16 mysite]# python manage.py migrate
MariaDB [dj1807]> show tables;
MariaDB [dj1807]> desc polls_question;
MariaDB [dj1807]> desc polls_choice;
数据库中的表名，结构是：应用名_类名
每张表都会自动生成名为id的主建字段。每个类变量成为表中的一个字段。
外键字段的名字是：类变量_id

3、修改外键名字
class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.choice_text, self.question)
(djenv) [root@room8pc16 mysite]# python manage.py makemigrations
(djenv) [root@room8pc16 mysite]# python manage.py migrate
MariaDB [dj1807]> desc polls_choice;


将模型注册到后台管理界面
1、修改polls/admin.py
from django.contrib import admin
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
2、在后台界面查看












python api
1、激活虚拟环境
[root@room8pc16 mysite]# source /opt/djenv/bin/activate
2、进入项目目录，运行python shell
(djenv) [root@room8pc16 mysite]# python manage.py shell
>>> from polls.models import Question, Choice
3、每个模型默认都有一个管理器，叫objects，用来对数据进行增删改查
4、查看所有的Question实例
>>> Question.objects.all()
5、添加新的问题
(1) 通过新建实例的方式创建
>>> from django.utils import timezone
>>> q1 = Question(
            question_text='春节有什么计划？', pub_date=timezone.now()
         )
>>> q1.save()
(2) 通过objects管理器创建
>>> q2 = Question.objects.create(
            question_text='散伙饭去哪吃？', pub_date=timezone.now()
        )
6、添加新的选项
(1) 通过新建实例的方式
>>> c1 = Choice(choice_text='加班', question=q1)
>>> c1.save()
(2) 通过objects管理器创建
>>> c2 = Choice.objects.create(choice_text='回家过年', question=q1)
(3) 通过问题直接创建选项。具体的问题比如是q1(春节有什么计划？)，因为Choice类有
外键，那么问题就有多个选项，q1也有一个管理器叫choice_set，如果选项的类名是C，那
么q1的管理器就叫c_set。这个管理器对应的就是该问题所有的选项。
>>> q1.choice_set.create(choice_text='外出旅游，逃避回家被催婚')

7、通过get查询，get要求只能返回一个结果，这个结果是一个实例
(1) 通过主键查询
>>> Question.objects.get(pk=1)
(2) 通过id查询
>>> Question.objects.get(id=2)  # id=2是id__exact=2的简写
(3) 通过其他字段查询
>>> Question.objects.get(question_text='你计划到哪个城市找工作？')
(4) 如果返回的结果是多项，将出现异常
>>> Question.objects.get(id__gte=2)
(5) 如果查不到，也会抛出异常
>>> Question.objects.get(id__exact=8)

注：双下划线是属性，python常用的取出属性是句点表示，如'对象.属性'；在django的条
件里，属性都是使用双下划线
>>> astr = '你计划到哪个城市找工作？'
>>> astr.startswith('你计划')
>>> Question.objects.get(question_text__startswith='你计划')
>>> astr.endswith('工作？')
>>> Question.objects.get(question_text__endswith='工作？')

8、获得排序的结果
order_by返回的结果是很多对象构成的查询集
(1) 通过pub_date进行排序，默认升序
>>> Question.objects.order_by('pub_date')
(2) 以降序的方式排列
>>> Question.objects.order_by('-pub_date')
(3) 查看对应的sql语句
>>> r1 = Question.objects.order_by('pub_date')
>>> print(r1.query)
(4) 获得最新的一个问题。降序的第一个实例，或升序的最后一个实例。注意查询集不支持负数索引
>>> Question.objects.order_by('-pub_date')[0]  或
>>> r1 = Question.objects.order_by('pub_date')
>>> r1[len(r1) - 1]

9、条件过滤
>>> Question.objects.filter(pub_date__year=2018)
>>> r3 = Question.objects.filter(pub_date__year=2018)
>>> print(r3.query)
>>> r3 = Question.objects.filter(pub_date__year=2018).filter(pub_date__month=12)
>>> print(r3.query)

10、修改和删除：首先找到对应的实例，修改就是属性重新赋值，删除是把对象直接删除
>>> q1 = Question.objects.get(question_text='你心仪的公司哪家？')
>>> q1.question_text = '你期望哪家公司给你发Offer？'
>>> q1.save()
>>> c1 = Choice.objects.get(choice_text='广州')
>>> c1.delete()

完成首页
1、修改视图函数，使之真正在数据库中取得所有的问题
# polls/views.py
from django.shortcuts import render
from .models import Question

def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})
2、在模板中显示所有的问题
# polls/templates/index.html
<body>
<h1>投票首页</h1>
<hr>
{{ questions }}
</body>
3、使用模板语言修改index.html
模块语言中，变量使用{{ var }}格式。其他标签使用{% %}，在{% %}中，变量不需要使
用双花括号。
# polls/templates/index.html
<body>
<h1>投票首页</h1>
<hr>
{% for question in questions %}
    <p>
        {{ forloop.counter }}. {{ question.question_text }} {{ question.pub_date }}
    </p>
{% endfor %}
</body>
注：forloop.counter是循环的计数

4、为问题添加超链接
# polls/templates/index.html
<body>
<h1>投票首页</h1>
<hr>
{% for question in questions %}
    <p>
        {{ forloop.counter }}.
{#        <a href="/polls/{{ question.id }}/">{{ question.question_text }}</a>#}
        <a href="{% url 'detail' question_id=question.id %}">{{ question.question_text }}</a>
        {{ question.pub_date }}
    </p>
{% endfor %}
</body>


完成详情页
1、修改视图函数，将问题传递到模板文件
def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'detail.html', {'question': question})
2、修改模板文件，显示问题及其选项
<body>
<h1>投票详情</h1>
<hr>
<h2>{{ question.question_text }}</h2>
<ul>
    {% for choice in question.choice_set.all %}
        <li>{{ choice.choice_text }}</li>
    {% endfor %}
</ul>
</body>
3、修改投票详情页，创建form表单
(1) 当用户投票时，将投票的数据发送到http://127.0.0.1/polls/1/vote/
# polls/urls.py
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
(2) http://127.0.0.1/polls/1/vote/对应成一个函数。该函数可以将相应选项的
票数加1
(3) 修改投票详情页，将上一步的UL改写为表单
<body>
<h1>投票详情</h1>
<hr>
<h2>{{ question.question_text }}</h2>
<form action="{% url 'vote' question_id=question.id %}" method="post">
    {% for choice in question.choice_set.all %}
        <div>
            <label>
                <input type="radio" name="choice_id" value="{{ choice.id }}">
                {{ choice.choice_text }}
            </label>
        </div>
    {% endfor %}
    <input type="submit" value="投 票">
</form>
</body>
(4) 编写投票函数，投票后跳转到投票详情页
from django.shortcuts import render, redirect

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    # request.POST可以理解为一个字典，通过get方法获取表单提交的数据
    choice_id = request.POST.get('choice_id')
    choice = question.choice_set.get(id=choice_id)
    choice.votes += 1
    choice.save()
    return redirect('result', question_id=question_id)
注意：此处没有使用render而是redirect。render将会把request请求中的数据再发给
相应的页面。redirect是独立的，不会发送任何数据。
(5) 上一步完成后，提交表单时，出现403禁止访问，可以关闭CSRF功能
# mysite/settings.py
MIDDLEWARE = [
    ... ...
    # 'django.middleware.csrf.CsrfViewMiddleware',
    ... ...
]
到此步完成，已经可以实现投票功能了。

完成投票结果页
1、完成函数
def result(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})
2、修改polls/templates/result.html
<body>
<h1>投票结果</h1>
<hr>
<h2>{{ question.question_text }}</h2>
<table border="1px">
    {% for choice in question.choice_set.all %}
        <tr>
            <td>{{ choice.choice_text }}</td>
            <td>{{ choice.votes }}</td>
        </tr>
    {% endfor %}
</table>
</body>















新建django项目
1、创建项目
(djenv) [root@room8pc16 day06]# django-admin startproject myblog
(djenv) [root@room8pc16 day06]# cd myblog/
2、新建应用
(djenv) [root@room8pc16 myblog]# python manage.py startapp blog
3、修改配置
# myblog/settings.py
ALLOWED_HOSTS = '*'
INSTALLED_APPS = [
    ... ...
    'blog',
]
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
4、启动服务进行测试
(djenv) [root@room8pc16 myblog]# python manage.py runserver 0:80

5、授权，以/blog/开头的URL授权给应用
# myblog/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
]
6、在应用中创建URLConfig文件
# blog/urls.py
from django.conf.urls import url

urlpatterns = [
]
7、以/blog/hello/对应hello函数
# blog/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/$', views.hello, name='hello'),
]
# blog/views.py
from django.shortcuts import render, HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')


RESTful API
http://www.runoob.com/w3cnote/restful-architecture.html
REST全称是Representational State Transfer，中文意思是表述（编者注：通常译为表征）性状态转移。
REST指的是一组架构约束条件和原则。REST本身并没有创造新的技术、组件或服务，
而隐藏在RESTful背后的理念就是使用Web的现有特征和能力，更好地使用现有Web标准中的一些准则和约束。

8、创建模型
# blog/models.py
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    text = models.TextField()

    def __str__(self):
        return self.title
(djenv) [root@room8pc16 myblog]# python manage.py makemigrations
(djenv) [root@room8pc16 myblog]# python manage.py migrate
9、创建管理员用户
(djenv) [root@room8pc16 myblog]# python manage.py createsuperuser
10、把模型注册到后台管理界面
# blog/admin.py
from django.contrib import admin
from .models import Blog

admin.site.register(Blog)

11、实现blog
(1) URL
    url(r'^$', views.index, name='index'),
(2) views.py
def index(request):
    return render(request, 'index.html')
(3) blog/templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>我的博客</title>
</head>
<body>
我的博客
</body>
</html>

12、修改视图函数，将文章取出发送到HTML模板
def index(request):
    articles = Blog.objects.order_by('-pub_date')
    return render(request, 'index.html', {'articles': articles})
13、修改模板文件index.html，显示文章
<body>
{% for article in articles %}
    <h2>{{ article.title }}</h2>
    <div>{{ article.pub_date }}</div>
    <div>{{ article.text }}</div>
{% empty %}
    <h2>尚无文章发布</h2>
{% endfor %}
</body>
14、发布文章时，时间不应该由用户手工书写，应该是程序自动添加。修改models.py
    pub_date = models.DateTimeField(auto_now_add=True)
(djenv) [root@room8pc16 myblog]# python manage.py makemigrations
(djenv) [root@room8pc16 myblog]# python manage.py migrate
15、在index.html中加入表单，实现发布文章的功能
<body>
<form action="" method="post">
    <label>标题：</label><input type="text" name="title"><br>
    <textarea name="content" cols="80" rows="10"></textarea><br>
    <input type="submit" value="发 布">
</form>
<hr>
{% for article in articles %}
    <h2>{{ article.title }}</h2>
    <div>{{ article.pub_date }}</div>
    <div>{{ article.text }}</div>
{% empty %}
    <h2>尚无文章发布</h2>
{% endfor %}
</body>

16、当表单提交数据时，会出现403CSRF失败，解决方法是在表单中加入验证。
<form action="" method="post">
    {% csrf_token %}
    <label>标题：</label><input type="text" name="title"><br>
    <textarea name="content" cols="80" rows="10"></textarea><br>
    <input type="submit" value="发 布">
</form>

17、接收网页POST过来的数据
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        #kenenghui chuang jian xiang tong wen zhang
        Blog.objects.get_or_create(title=title, text=content)

    articles = Blog.objects.order_by('-pub_date')
    return render(request, 'index.html', {'articles': articles})

18、博客正文没有分段，修正该问题，可以在模板文件中使用过滤功能
将以下行：
    <div>{{ article.text }}</div>
修改为：
    <div>{{ article.text|linebreaks }}</div>












新建django项目
1、创建项目
(djenv) [root@room8pc16 day06]# django-admin startproject myblog
(djenv) [root@room8pc16 day06]# cd myblog/
2、新建应用
(djenv) [root@room8pc16 myblog]# python manage.py startapp blog
3、修改配置
# myblog/settings.py
ALLOWED_HOSTS = '*'
INSTALLED_APPS = [
    ... ...
    'blog',
]
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
4、启动服务进行测试
(djenv) [root@room8pc16 myblog]# python manage.py runserver 0:80

5、授权，以/blog/开头的URL授权给应用
# myblog/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
]
6、在应用中创建URLConfig文件
# blog/urls.py
from django.conf.urls import url

urlpatterns = [
]
7、以/blog/hello/对应hello函数
# blog/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/$', views.hello, name='hello'),
]
# blog/views.py
from django.shortcuts import render, HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')


RESTful API
http://www.runoob.com/w3cnote/restful-architecture.html
REST全称是Representational State Transfer，中文意思是表述（编者注：通常译为表征）性状态转移。
REST指的是一组架构约束条件和原则。REST本身并没有创造新的技术、组件或服务，
而隐藏在RESTful背后的理念就是使用Web的现有特征和能力，更好地使用现有Web标准中的一些准则和约束。

8、创建模型
# blog/models.py
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    text = models.TextField()

    def __str__(self):
        return self.title
(djenv) [root@room8pc16 myblog]# python manage.py makemigrations
(djenv) [root@room8pc16 myblog]# python manage.py migrate
9、创建管理员用户
(djenv) [root@room8pc16 myblog]# python manage.py createsuperuser
10、把模型注册到后台管理界面
# blog/admin.py
from django.contrib import admin
from .models import Blog

admin.site.register(Blog)

11、实现blog
(1) URL
    url(r'^$', views.index, name='index'),
(2) views.py
def index(request):
    return render(request, 'index.html')
(3) blog/templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>我的博客</title>
</head>
<body>
我的博客
</body>
</html>

12、修改视图函数，将文章取出发送到HTML模板
def index(request):
    articles = Blog.objects.order_by('-pub_date')
    return render(request, 'index.html', {'articles': articles})
13、修改模板文件index.html，显示文章
<body>
{% for article in articles %}
    <h2>{{ article.title }}</h2>
    <div>{{ article.pub_date }}</div>
    <div>{{ article.text }}</div>
{% empty %}
    <h2>尚无文章发布</h2>
{% endfor %}
</body>
14、发布文章时，时间不应该由用户手工书写，应该是程序自动添加。修改models.py
    pub_date = models.DateTimeField(auto_now_add=True)
(djenv) [root@room8pc16 myblog]# python manage.py makemigrations
(djenv) [root@room8pc16 myblog]# python manage.py migrate
15、在index.html中加入表单，实现发布文章的功能
<body>
<form action="" method="post">
    <label>标题：</label><input type="text" name="title"><br>
    <textarea name="content" cols="80" rows="10"></textarea><br>
    <input type="submit" value="发 布">
</form>
<hr>
{% for article in articles %}
    <h2>{{ article.title }}</h2>
    <div>{{ article.pub_date }}</div>
    <div>{{ article.text }}</div>
{% empty %}
    <h2>尚无文章发布</h2>
{% endfor %}
</body>

16、当表单提交数据时，会出现403CSRF失败，解决方法是在表单中加入验证。
<form action="" method="post">
    {% csrf_token %}
    <label>标题：</label><input type="text" name="title"><br>
    <textarea name="content" cols="80" rows="10"></textarea><br>
    <input type="submit" value="发 布">
</form>

17、接收网页POST过来的数据
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Blog.objects.get_or_create(title=title, text=content)

    articles = Blog.objects.order_by('-pub_date')
    return render(request, 'index.html', {'articles': articles})

18、博客正文没有分段，修正该问题，可以在模板文件中使用过滤功能
将以下行：
    <div>{{ article.text }}</div>
修改为：
    <div>{{ article.text|linebreaks }}</div>


www.conyli.cc/django-2.-by-example ==> django develop








</pre>
