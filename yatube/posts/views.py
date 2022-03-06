from django.shortcuts import render, get_object_or_404

from .models import Group, Post


def index(request):
    template = 'posts\index.html'
    text = "Это главная страница проекта Yatube"
    context = {
        'text': text
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts\group_list.html', context)

