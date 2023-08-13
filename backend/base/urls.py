from django.urls import path
from base import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.getCategories, name='categories'),
    path('news/', views.getNews, name='news'),
]
