from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import Http404, HttpResponse
from .models import Movie, Genre, Review
from .forms import MovieForm, ReviewForm


# Create your views here.
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

    