#django imports style guide
# 1 . standard library
# 2. third party
# 3. django
# 4. local django


import random
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request): #첫번째 인자는 반드시 request
    return render(request, 'index.html') #render()의 첫번째 인자도 request


def introduce(request, name, age):
    context = {'name' : name, 'age' : age}
    return render(request, 'introduce.html', context)


def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick':pick}
    return render(request, 'dinner.html', context)


def image(request):
    return render(request, 'image.html')


def hello(request, name):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'name' : name,'pick':pick}
    return render(request, 'hello.html', context)


def times(request, a, b):
    context = {'a':a, 'b':b, 'times':a*b}
    return render(request, 'times.html',context)


def area(request, r):
    context = {'r':r, 'area':(r**2)*3.14}
    return render(request, 'area.html',context)

def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피',]
    my_sentence = 'llfe is short, you need python'
    message = ['apple', 'banana', 'cucumber', 'bean']
    datetimenow = datetime.now()
    empty_list =[]
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'message' : message,
        'datetimenow' : datetimenow,
        'empty_list' : empty_list
    }
    return render(request, 'template_language.html', context)


def isitgwangbok(request):
    td_date = datetime.now()
    if td_date.month == 8 and td_date == 15:
        result = True
    else:
        result = False
    context = {'result':result, 'td_date':td_date}

    return render(request, 'checkgbd.html',context)