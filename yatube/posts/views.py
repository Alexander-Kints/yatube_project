from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    template = 'posts\index.html'
    text = "Это главная страница проекта Yatube"
    context = {
        'text': text
    }
    return render(request, template, context)


def group_posts(request):
    template = 'posts\group_list.html'
    return render(request, template)


def group_post(request, slug):
    return HttpResponse(f'{slug}')
