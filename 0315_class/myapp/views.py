from django.shortcuts import render
import random

# Create your views here.

def index(request,nick):

    context = {
        'name':nick
    }

    return render(request,'myapp/index.html',context)

def greeting(request):
    
    foods = ['apple','banana','mango',]
    info = {
        'name':'kevin'
    }

    pick = random.choice(foods)
    context = {
        'foods' : foods,
        'info': info,
        'pick' : pick,
    }

    return render(request,'myapp/greeting.html',context)