from . import views
from django.urls import path

app_name='movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.movie_detail, name='detail'),
    path('<int:movie_pk>/reviews/new/', views.review_create, name='review_create'),
    path('<int:movie_pk>/reviews/<int:review_pk>/delete/', views.review_delete, name='review_delete'),
]
