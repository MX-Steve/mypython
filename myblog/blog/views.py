from django.shortcuts import render, HttpResponse
from .models import Blog

# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')

def welcome(request, name ):
    return HttpResponse('<h1>this is %s</h1>'%name)

def index(request):
    if request.method=='POST':
        title = request.POST.get("title")
        content = request.POST.get('content')
        Blog.objects.get_or_create(title=title, text=content)
    articles = Blog.objects.order_by('-pub_date')
    return render(request, 'index.html', {'articles': articles})