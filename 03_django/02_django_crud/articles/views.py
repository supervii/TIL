from IPython import embed
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk') # DB 가 변경한 것
    # articles = Article.objects.all()[::-1] # python 이 변경한 것
    context ={'articles':articles,}
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')


def create(request):
    try:
        title = request.POST.get('title')
        content = request.POST.get('content')
    
    
    
    # pk = request.POST.get('pk')
    # 1
    # article= Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2
        article = Article(title=title, content=content)
        article.full_clean() # 유효성 검증. 
        # is_valid()
    except ValidationError:
        raise ValidationError('ERROR!!!!')
    else:
        article.save()

    #3
    # Article.objects.create(title=title, content=content)

        return redirect(f'/articles/{article.pk}/')
        

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article':article,}
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/articles/')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article':article,}
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect(f'/articles/{article.pk}/')