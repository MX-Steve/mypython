from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('<h1>polls index</h1>')
    return  render(request,'index.html')

def details(request):
    return render(request,'details.html')

def result(request):
    return render(request,'result.html')