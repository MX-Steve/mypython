from django.shortcuts import render

# Create your views here.

def index(request):
    # return HttpResponse('<h1>xxx</h1>')
    return render(request, 'index.html')