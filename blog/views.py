from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {'author': 'jan',
     'title': 'title1',
     'content': 'first content',
     'date_posted': 'date1'},
    {'author': 'paul',
     'title': 'title2',
     'content': 'second content',
     'date_posted': 'date2'},


]


def home(request):
    # return HttpResponse('<h1> Blog home </h1>')
    context = {'posts': posts}

    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1> About page</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
