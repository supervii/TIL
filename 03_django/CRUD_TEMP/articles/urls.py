from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'), # NEW(GET) +CREATE(POST)
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:article_pk>/update/', views.update, name='update'), #EDIT(GET)+ UPDATE(POST)
    path('<int:article_pk>/comments/', views.comment_create, name='comment_create'), # DETAIL(GET) + CREATE(POST)
    path('<int:article_pk>/<int:cmt_pk>/comments_del/', views.comments_delete, name='comments_delete'), # DETAIL(GET) + CREATE(POST)



]
