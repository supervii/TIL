from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="Movie API",
      default_version='v1',
      description="영화 정보 API 입니다.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="movies@ssafy.com"),
      license=openapi.License(name="SSAFY License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = 'movies'
urlpatterns = [
   path('genres/', views.genre_list, name='genre_list'),
   path('genres/<int:genre_pk>/', views.genre_detail, name='genre_detail'),
   path('movies/', views.movie_list, name='movie_list'),
   path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
   path('movies/<int:movie_pk>/reviews/', views.review_create, name='review_create'),
   path('reviews/<int:review_pk>/', views.review_update_delete, name='review_update_delete'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
