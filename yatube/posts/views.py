from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница с постами')


def group_posts(request,slug):
    return HttpResponse(f'Посты об {slug}')
