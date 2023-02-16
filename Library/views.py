from django.shortcuts import render

# Create your views here.

def base(request):
    res = render(request,'base.html')
    return res

def student_registor(request):
    res = render(request,'student_registor.html')
    return res
def find_books(request):
    res = render(request,'search_book.html')
    return res

def available_books(request):
    res = render(request,'available_book.html')
    return res 
