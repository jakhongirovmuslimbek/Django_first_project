from django.urls import path
from .views import uz_page, gl_page, sp_page, my_func, HomePageView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('news/', my_func, name='news'),
    path('uzbekistan/', uz_page, name='uz'),
    path('global/', gl_page, name='global'),
    path('sport/', sp_page, name='sport'),
]
