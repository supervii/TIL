# 데이터베이스 설계|프로젝트

### 1. 프로젝트 소개 &#128195;

본 프로젝트는 협업을 통해 데이터베이스 모델링 및 기능을 구현하고 다양한 형태의 데이터 베이스 관계를 설정하는 과정입니다. 협업의 핵심은 내 고집, 내가 하고 싶은 것만 이야기하는것이 아니라, 동료인 '남'의 말을 듣고, 그의 의견을 따라서 움직이는 것을 더 중요하게 여기는 것이 협업입니다. 서로의 경험과 지식, 전문성을 중요시하여 각자의 전문 분야를 인정할 수 있어야 합니다. 

 

### 2. 과정 및 파일에 대한 설명

##### 1. 데이터베이스 설계

다음 형식으로 데이터베이스의 모델을 설계합니다.

```python
class Genre(models.Model):
   name = models.CharField(max_length=50)
   def __str__(self):
       return self.name
class Movie(models.Model):
   title = models.CharField(max_length=50)
   audience = models.IntegerField()
   poster_url = models.TextField()
   description = models.TextField()
   genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
   def __str__(self):
       return self.title
class Review(models.Model):
   content = models.CharField(max_length=50)
   score = models.IntegerField()
   movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   def __str__(self):
       return self.content
```

> Genre - name
>
> Movie - title, audience, poster_url, description, genre_id
>
> Review - content, score, movie, user



##### 2. Seed Data 반영

프로젝트에 주어진 `movie.json` 과`genre.json` 을 통해 Seed Data를 반영 후, admin.py에 클래스를 등록한 후, 데이터 반영을 확인할 수 있었습니다. 

새로운 명령어를 사용하였기에 학습이 필요했습니다. (loaddata)



##### 3. `accounts` App

유저의 회원가입과 로그인, 로그아웃 기능을 구현하고 /accounts.html 과 /accounts/detail.html을 만들어 사용자 목록을 보여주고 , 사용자를 클릭하면 유저 상세보기 페이지(accounts/detail.html)로 넘어 갈수 있게 구현합니다.

사용자 목록을 표시하는데 어려움은 없었지만 유저의 상세한 평점 정보를 가져오는데 어려움이 있었습니다.

```python
def signup(request):
   if request.user.is_authenticated:
       return redirect('accounts:user_list')
   if request.method == 'POST':
       form = CustomUserCreationForm(request.POST)
       if form.is_valid():
           user = form.save()
           auth_login(request, user)
           return redirect('accounts:user_list')
   else:
       form = CustomUserCreationForm()
   context = {'form': form,}
   return render(request, 'accounts/auth_form.html', context)
def login(request):
   if request.user.is_authenticated:
       return redirect('accounts:user_list')
   if request.method == 'POST':
       form = AuthenticationForm(request, request.POST)
       if form.is_valid():
           auth_login(request, form.get_user())
           return redirect(request.GET.get('next') or 'accounts:user_list')
   else:
       form = AuthenticationForm()
   context = {'form': form,}
   return render(request, 'accounts/auth_form.html', context)
def logout(request):
   auth_logout(request)
   return redirect('accounts:user_list')
def user_list(request):
   users = User.objects.all()
   context = {'users': users,}
   return render(request, 'accounts/user_list.html', context)
def user_detail(request, user_pk):
   users = get_object_or_404(get_user_model(), pk=user_pk)
   reviews = users.review_set.all()
   context = {'users': users, 'reviews': reviews,}
   return render(request, 'accounts/detail.html', context)
```

디테일 부분에서 _set.all 구문으로 데이터를 전송하는데 있어서 오류가 있었지만 지속적인 소통을 통해 고칠 수 있었습니다. 

##### 4. `movies`App

영화 목록을 보여주고 , 영화 목록에서 이미지를 클릭하면 영화 상세보기로 넘어갑니다. 상세보기에는 영화관련 정보가 모두 나열되며, 로그인한 사람만 평점을 남길 수 있고, 모든 사람은 평점 목록을 볼 수 있습니다. 영화가 존재하지 않을 경우는 404 페이지를 보여줍니다. 또한 평점을 생성해주고 평점 삭제는 본인만 할 수 있습니다.  

```python
def index(request):
   movies = Movie.objects.all()
   context = {'movies': movies,}
   return render(request, 'movies/index.html', context)
def movie_detail(request, movie_pk):
   movie = get_object_or_404(Movie, pk=movie_pk)
   reviews = movie.review_set.all()
   review_form = ReviewForm()
   context = {'movie': movie, 'reviews': reviews, 'review_form': review_form,}
   return render(request, 'movies/movie_detail.html', context)
@login_required
def review_create(request, movie_pk):
   if request.user.is_authenticated:
       review_form = ReviewForm(request.POST)
       if review_form.is_valid():
           review = review_form.save(commit=False)
           review.movie_id = movie_pk
           review.user_id = request.user.pk
           review.save()
   return redirect('movies:detail', movie_pk)
@require_POST
def review_delete(request, movie_pk, review_pk):
   if request.user.is_authenticated:
       review = get_object_or_404(Review, pk=review_pk)
       if request.user == review.user:
           review.delete()
           return redirect('movies:detail', movie_pk)
       else:
           return redirect('movies:detail', movie_pk)
   return HttpResponse('You are Unauthorized', status=401)
```



##### 결과물 

![]( https://user-images.githubusercontent.com/52684457/67735279-fcf3c680-fa46-11e9-8fb3-f7c23420e667.png )

 ![](https://user-images.githubusercontent.com/52684457/67738015-7fcd4f00-fa50-11e9-8775-391ce9ad8765.png)



 ![]( https://user-images.githubusercontent.com/52684457/67735299-0aa94c00-fa47-11e9-9a4f-8c0a4b700c90.png ) 

 ![]( https://user-images.githubusercontent.com/52684457/67735316-1bf25880-fa47-11e9-9ab1-25171eb4a350.png ) 



### 프로젝트를 통해 느낀 점

처음으로 프로젝트를 협업으로 진행하면서 커뮤니케이션 능력의 중요성을 다시 한번 알게되었습니다.  서로가 알고 있는 부분이 달라 하나하나 비교해가면서 찾아가는데 더 많은 시간이 소비되었지만, 점차 가속을 붙여 혼자하는 것보다 더 효율적인 방법을 서로 배울 수 있었습니다. 데이터 베이스의 모델링과 관계 설정을 통해 성공적으로 프로젝트를 마감할 수 있었습니다 .