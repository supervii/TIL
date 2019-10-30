from . import views
from django.urls import path

app_name='accounts'
urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/', views.user_detail, name='detail'),
]
