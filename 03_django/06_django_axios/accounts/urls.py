from django.urls import path
from . import views

app_name ='accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('<username>', views.profile, name='profile'), # 임의의 문자열을 읽어오는 주소이기 때문에 맨 아래에 있어야한다 위에 있으면 page not found 

]
