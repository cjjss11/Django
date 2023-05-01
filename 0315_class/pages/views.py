from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def hello(request):
    return render(request, 'pages/hello.html')
