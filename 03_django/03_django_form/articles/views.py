from IPython import embed
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        # form 인스턴트를 생성하고 요청에 의한 데이터를 인자로 받는다.(binding)
        # 이 처리 과정은 binding 이라고  불리며 유효성 체크를 할 수 있도록 해준다.
        form = ArticleForm(request.POST)
        # form이 유효한지 체크한다.
        if form.is_valid():
            # form.cleand_data 로 정제된 데이터를 받는다.
            article = form.save()
            return redirect(article)
    else:
        form = ArticleForm()
    #  상황에 따라 context 에 넘어가는 2가지 form
    #  1. GET : 기본 form
    #  2. POST : 검증에 실패 후 의 form(is_vaild == False) 
    context = {'form':form,}
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all #article 의 모든 댓글
    comment_form = CommentForm() #댓글 폼
    context = {'article':article, 'comment_form':comment_form, 'comments':comments}
    return render(request, 'articles/detail.html',context)

@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')
    

def update(request, article_pk):
    article = get_object_or_404(Article, pk =article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        # ArticleForm 을 초기화 (이전에 DB에 저정된 데이터를 넣어준 상태)
        # form = ArticleForm(initial={'title':article.title, 'content':article.content})
        # __dict__ : article 객체 데이터를 딕셔너리 자료형으로 변환
        form = ArticleForm(instance=article)
    # 1. POST: 검증에 실패한 form(오류 메세지도 포함된 상태)
    # 2. GET: 초기화된 form
    context = {'form':form, 'article':article,}
    return render(request, 'articles/form.html', context)

@require_POST
def comment_create(request, article_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # 객체를 create 하지만, db에 레코드는 작성하지 않는다.
        comment = comment_form.save(commit=False)
        comment.article_id = article_pk
        comment.save()
    return redirect('articles:detail', article_pk)
    

@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk =comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)