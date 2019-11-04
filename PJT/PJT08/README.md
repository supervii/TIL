# REST API|프로젝트

### 1. 프로젝트 소개 📃

본 프로젝트는 Python Web Framework를 사용합니다. API 요청에 대한 이해를 통해 RESTful API서버를 구축하고 API를 문서화 하는 과정을 나타냅니다. 데이터베이스 설계와 Seed 데이터 반영하고 결과 응답 및 에러 메세지를 생성합니다.

REST

>REST는 SOAP이 서비스 지향 구조인 것과 달리 자원지향구조(ROA: Resource Oriented Architecture)로 웹 사이트의 컨텐츠(Text, 이미지, 동영상), DB의 내용 등을 전부 하나의 자원으로 파악하여 각 자원의 고유한 URI(Uniform Resource Identifier)를 부여하고, 해당 자원에 대한 CRUD(Create, Read, Update, Delete) 작업을 HTTP의 기본 명령어인 POST, GET, PUT, DELETE를 통해서 처리한다.

### 2.과정 및 파일에 대한 설명

- 먼저 데이터 베이스 설계를 위해 모델을 작성합니다. 

```python
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('pk',)


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=1000)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        ordering = ('pk',)


class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=200)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)    

    class Meta:
        ordering = ('-pk',)
```

- 주어진 movie.json, genre.json을 movies/fixtures 디렉토리로 이동 시켜 seed data 를 반영해줍니다.

```bash
 $ python manage.py loaddata genre.json 
 $ python manage.py loaddata movie.json
```

- admin.py 에 genre, movie 클래스를 등록해줍니다.

- 또한 시드 데이터를 적용하고 리스트 하나하나를 json 타입으로 바꿔주기 위해서 Serializer.py를 작성한다 .

```python
from rest_framework import serializers
from .models import Genre, Movie, Review

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name',)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'audience', 'poster_url', 'description', 'genre_id',)


class GenreDetailSerializer(GenreSerializer):
    movies = MovieSerializer(source='movie_set', many=True)

    class Meta(GenreSerializer.Meta):
        fields = ('id', 'movies', 'name',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'content', 'score', 'movie_id',)


class MovieDetailSerializer(MovieSerializer):
    reviews = ReviewSerializer(source='review_set', many=True)

    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields + ('reviews',)
```



- urls.py를 작성하는데 있어 전의 과정과 달리 import 해오는 것이 많아 숙지할 점이 많았습니다.

```python
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

```





#### 결과물

![Screen Shot 2019-11-01 at 12 24 44 PM](https://user-images.githubusercontent.com/52685245/68000246-af739580-fca2-11e9-8654-1fb4dfada733.png)





### 3. 프로젝트를 통해 느낀 점

Web Framework를 통해 API 요청을 통해 API 서버를 구축하고 API를 문서화 하는 과정이 미숙하여 코딩을 하는데 있어 시간이 많이 소비되었습니다.  Serializer.py 작성에 있어 학습이 미흡하여, 꾸준한 복습을 통해 개발시켜야할 필요성에 대해 느꼈습니다. 또한 REST 기반의 아키텍처를 설계하려면 가장 어려운 것이 이 URI를 어떻게 정의하는 것이라고 생각합니다. REST의 장점 중 하나는 이 URI와 HTTP Method만으로도 쉽게 의미를 파악할 수 있다는 것이기 때문에, URI 정의에 많은 노력이 필요할 것입니다.

### 