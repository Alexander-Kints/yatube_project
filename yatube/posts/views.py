from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    template = 'posts\index.html'
    return render(request, template)


def group_posts(request):
    return HttpResponse('Тут у нас список постов будет.')


def group_post(request, slug):
    return HttpResponse(f'{slug}')
