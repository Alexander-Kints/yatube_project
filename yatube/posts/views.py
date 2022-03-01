from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request):
    return HttpResponse('Тут у нас список постов будет.')


def group_post(request, slug):
    return HttpResponse(f'{slug}')
