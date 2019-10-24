from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Hashtag(models.Model):
    # 같은 해시태그가 작성되면 안됌(unique)
    # unique =True 인 경우 이 필드는 테이블 전체에서 고유한 값이어야 한다.
    # 유효성 검사 단계에서 실행되며 중복값이 있는 모델을 저장하려고 하면 .save()메서드로 인해 IntergrityError가 발생한다.
    # ManytoManyField 및 OneToOneField를 제외한 나머지에서 사용 가능 
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name= 'like_articles', blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)


    class Meta:
        ordering = ('-pk',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"article_pk": self.pk})

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length= 140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']
    
    def __str__(self):
        return self.content
        # return f'<Article({self.article_id}): Comment({self.pk})-{self.content}'
