## Django, Model, ORM 을 포함한 CRUD 기능 구현 |프로젝트

### 1. 프로젝트 소개 &#128195;

 본 프로젝트는 Django, Model, ORM을 활용하여 데이터를 Create, Reas, Update, Delete 기능을 하는 Web Application을 제작하는 것이 목표입니다. Python Web Framework를 통해 데이터를 조작하고 Template Variable을 활용하여 Template를 제작하였습니다. 기존의 영화 추천 데이터를 활용하여 영화 정보 데이터를 관리 할 수 있습니다.



### 2. 과정 및 파일에 대한 설명

1. ###### 가상환경을 먼저 구축하여 프로젝트 생성 및 앱을 생성해줍니다.(앱 등록, 앱 url 설정)

2. ###### models.py 에 로직에 맞추어 필요한 내용을 작성하여 줍니다 .

   ```python
   from django.db import models
   
   
   # Create your models here.
   class Movie(models.Model):
       title = models.CharField(max_length=20)
       title_en = models.CharField(max_length=20)
       audience = models.IntegerField()
       open_date = models.DateField()
       genre = models.CharField(max_length=20)
       watch_grade = models.CharField(max_length=10)
       score = models.FloatField()
       poster_url = models.TextField()
       description = models.TextField()
   
       def __str__(self):
           return self.title
   
   ```

3. ###### migration과 migrate 과정을 통해 설계도를 만들어 줍니다.

4. ###### superuser를 생성하여 admin 페이지를 만들어 줍니다.

5. ###### 앱의 views.py에서 필요한 함수들을 만들어 주고 필요한 templates, html, 앱 내 urls.py를 작성합니다.

   ```python
   from django.shortcuts import render, redirect
   from .models import Movie
   
   # Create your views here.
   def index(request):
       movies = Movie.objects.all()
       context = {'movies': movies}
       return render(request, 'movies/index.html', context)
   
   def new(request):
       return render(request, 'movies/new.html')
   
   def create(request):
       title = request.POST.get('title')
       title_en = request.POST.get('title_en')
       audience = request.POST.get('audience')
       open_date = request.POST.get('open_date')
       genre = request.POST.get('genre')
       watch_grade = request.POST.get('watch_grade')
       score = request.POST.get('score')
       poster_url = request.POST.get('poster_url')
       description = request.POST.get('description')
       
       movie = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
       movie.save()
   
       return redirect('/movies/')
   
   
   def detail(request, pk):
       movie = Movie.objects.get(pk=pk)
       context = {'movie':movie,}
       return render(request, 'movies/detail.html', context)
   
   def delete(request, pk):
       movie = Movie.objects.get(pk=pk)
       movie.delete()
       return redirect('/movies/')
   
   def edit(request, pk):
       movie = Movie.objects.get(pk=pk)
       context = {'movie':movie,}
       return render(request, 'movies/edit.html', context)
   
   def update(request, pk):
       movie = Movie.objects.get(pk=pk)
       movie.title = request.POST.get('title')
       movie.title_en = request.POST.get('title_en')
       movie.audience = request.POST.get('audience')
       movie.open_date = request.POST.get('open_date')
       movie.genre = request.POST.get('genre')
       movie.watch_grade = request.POST.get('watch_grade')
       movie.score = request.POST.get('score')
       movie.poster_url = request.POST.get('poster_url')
       movie.description = request.POST.get('description')
       
       movie.save()    
       return redirect(f'/movies/{ movie.pk }/')
   
   
   ```

6. ###### HTML 파일들을 프로젝트 내 base.html에 연결시켜주어 필요한 기능들을 구현합니다. 

   >index.html
   >
   >new.html
   >
   >detail.html
   >
   >edit.html

7. ###### 요구사항

>###### 데이터베이스
>
>ORM을 통해서 작성될 클래스의 이름은 Movie 이며, csv를 통해 가져온 데이터를 자료형에 맞게 넣어 줍니다.
>
>###### 페이지
>
>영화 목록
>
>해당 페이지에 접근하는 URL은 /movies/ 입니다.
>
>데이터베이스에 존재하는 모든 영화의 목록이 표시 되며, 각 영화의 title , score 가 표시됩니다.
>
>title 을 클릭 시, 해당 영화 정보 조회 페이지로 이동합니다.
>
> 영화 목록 최상단에 새 영화 등록 링크가 있으며, 클릭 시 영화 정보 생성 Form 페이지로 이동합니다.
>
>###### 영화 정보 생성 Form
>
>해당 페이지에 접근하는 URL은 /movies/new/ 입니다.
>
>영화 정보를 작성할 수 있는 Form이 표시 되며, csv를 통해 가져온 데이터를 input에 넣어줍니다.
>
>Form에 작성된 정보는 Form Submit 버튼 클릭 시 영화 정보 생성 페 이지로 생성 요청(request)과 함께 전송됩니다.
>
>######  영화 정보 조회
>
>해당 페이지에 접근하는 URL은 /movies/1/ , /movies/2/ 등 이며, 동 적으로 할당되는 부분이 존재합니다. 동적으로 할당되는 부분에는 데이터베 이스에 저장된 영화 정보의 Primary Key가 들어갑니다.
>
>해당 Primary Key를 가진 영화의 모든 정보가 표시됩니다.
>
>영화 정보의 최하단에는 목록 , 수정 , 삭제 링크가 있으며, 클릭 시 각각 영화 목록 , 해당 영화 정보 수정 Form , 해당 영화 정보 삭제 페이지로 이동합니다.
>
>######  영화 정보 수정 Form
>
>해당 페이지에 접근하는 URL은 /movies/1/edit/ , /movies/2/edit/ 등 이며, 동적으로 할당되는 부분이 존재합니다. 동적으로 할당되는 부분에는 데이터베이스에 저장된 영화 정보의 Primary Key가 들어갑니다.
>
>해당 Primary Key를 가진 영화 정보를 수정할 수 있는 Form이 표시 되며, 정보가 입력된 채로 다음과 같은 input들을 가지고 있습니다.
>
>######  영화 정보 삭제
>
> 해당 페이지에 접근하는 URL은 /movies/1/delete/ , /movies/2/delete/ 등 이며, 동적으로 할당되는 부분이 존재합니다. 동적으 로 할당되는 부분에는 데이터베이스에 저장된 영화 정보의 Primary Key가 들어갑니다.
>
>해당 Primary Key를 가진 영화 정보를 데이터베이스에서 삭제합니다.
>영화 정보 목록 페이지로 Redirect 합니다.



######  어려웠던 점. 

큰 설계도에 따라 여러가지 기능을 구현해야하기 때문에 render와 redirect에 있어서 혼동이 있었지만 시행착오를 통해 완성 시킬 수 있었습니다. 또한, 데이터를 수정하는 과정에서 원래 데이터값을 불러오기와 덮어씌우기에 대해 더 신경써야했습니다. 

##### 결과물



![1](https://user-images.githubusercontent.com/52685245/63579625-0fc4c780-c5ce-11e9-96e2-808ccd4d41f6.JPG)

![2](https://user-images.githubusercontent.com/52685245/63579650-1b17f300-c5ce-11e9-9acc-fc854cf0b6e9.JPG)

![3](https://user-images.githubusercontent.com/52685245/63579675-2408c480-c5ce-11e9-931e-dc49147e6b67.JPG)

![4](https://user-images.githubusercontent.com/52685245/63579695-2c60ff80-c5ce-11e9-8157-fff3d8ee3203.JPG)

### 3. 프로젝트를 통해 느낀점

django, ORM, Model을 활용하여 CRUD 기능을 구현할 수 있었습니다. 다소 미흡한점이 많았지만 , 꾸준한 반복을 통해 과정에 익숙해져야 할 필요성을 느꼈습니다.