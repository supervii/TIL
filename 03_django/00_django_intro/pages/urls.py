from django.urls import path
from . import views

urlpatterns = [
    # app url 은 아래도 작성한다
    path('index/', views.index), # url 경로 마지막에 / 를 붙이는 습관 
    path('intro/<name>/<age>', views.introduce),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('hello/<name>/', views.hello),
    path('template_language/', views.template_language),
    path('times/<int:a>/<int:b>/', views.times),
    path('area/<int:r>/', views.area),
    path('isitgbd/', views.isitgwangbok),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]