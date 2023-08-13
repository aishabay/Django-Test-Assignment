from django.urls import path
from base import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.getCategories, name='categories'),
    path('news/', views.getNews, name='news'),
    path('news/the-most-popular/', views.getTheMostPopularNews, name='news-the-most-popular'),
    # path('display-image', views.display_image, name='image'),
]
