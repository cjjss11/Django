from django.shortcuts import render
# import random

def certification1(request):
    ages = range(25,31)
    grades = ['a','b','c','s',]
    name = 'kim happy'

    context = {
        'ages' : ages,
        'grades' : grades,
        'name' : name,
    }
    return render(request,'certification/certification1.html',context)

def certification2(request):
    ages = range(25,31)
    grades = ['a','b','c','s',]
    name = 'park happy'
    

    context = {
        'ages' : ages,
        'grades' : grades,
        'name' : name,
    }

    return render(request,'certification/certification2.html',context)

def certification3(request):
    ages = range(25,31)
    grades = ['a','b','c','s',]
    name = 'lee happy'
    
    context = {
        'ages' : ages,
        'grades' : grades,
        'name' : name,
    }

    return render(request,'certification/certification3.html',context)

# Create your views here.
