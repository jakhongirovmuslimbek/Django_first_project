from django.shortcuts import render
from my_app.models import *
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'


def my_func(request):
    data = {

    }
    return render(request, 'news/news.html', data)

def uz_page(request):
    news = UzbekistanNews.objects.all()
    data = {
        'uz_news': news, 

    }
    return render(request, 'news/uznews.html', data)

def gl_page(request):
    news = GlobalNews.objects.all()
    data = {
        'gl_news': news,

    }
    return render(request, 'news/glnews.html', data)

def sp_page(request):
    news = SportNews.objects.all()
    data = {
        'sp_news': news, 

    }
    return render(request, 'news/spnews.html', data)


