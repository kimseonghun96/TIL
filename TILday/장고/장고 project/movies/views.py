from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie' : movie
    }

    return render(request, 'movies/index.html', context)


def new(request):
    return render(request, 'movies/new.html')


def create(request):
    title = request.POST.get(title)
    context =  request.POST.get(context)

    return redirect('movies:index')


def edit(request):
    return render(request, 'movies/edit.html')

def detail(request):
    
    return render(request, 'movies/detail.html')

def delete(request, pk):
    article = Movie.objects.get(pk=pk)
    article.delete()
    return redirect(request, 'movies:index')

