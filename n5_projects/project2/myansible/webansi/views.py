from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def mainpage(request):
    return  render(request, 'mainpage.html')