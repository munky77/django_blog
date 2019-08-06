from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    # return HttpResponse('<h1> Blog home </h1>')
    context = {'posts': Post.objects.all()}

    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1> About page</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
