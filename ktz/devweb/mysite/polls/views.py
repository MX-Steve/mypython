from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('<h1>polls index</h1>')
    return  render(request,'index.html')

def details(request,question_id):
    return render(request,'details.html',{'question_id':question_id})

def result(request,question_id):
    return render(request,'result.html',{'question_id':question_id})