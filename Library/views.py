from django.shortcuts import render

# Create your views here.

def base(request):
    res = render(request,'base.html')
    return res

def student_registor(request):
    res = render(request,'student_registor.html')
    return res
