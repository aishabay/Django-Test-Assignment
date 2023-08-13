from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from base.models import Category, News
from base.serializers import CategorySerializer, NewsSerializer


def index(request):
    popularity_level_1_news = News.objects.filter(popularity_level=1).order_by('-createdAt')[:1]
    popularity_level_2_news = News.objects.filter(popularity_level=2).order_by('-createdAt')[:6]
    news = News.objects.order_by('-createdAt')[:10]

    show_business_news = News.objects.filter(category__name="Шоу Биз").order_by('-createdAt')[:4]
    
    economics_news_1 = News.objects.filter(category__name="Экономика").order_by('-createdAt')[:1]
    economics_news_others = News.objects.filter(category__name="Экономика").order_by('-createdAt')[1:4]

    society_news = News.objects.filter(category__name="Общество").order_by('-createdAt')[:4]

    world_news = News.objects.filter(category__name="В мире").order_by('-createdAt')[:4]

    politics_news_1 = News.objects.filter(category__name="Политика").order_by('-createdAt')[:1]
    politics_news_others = News.objects.filter(category__name="Политика").order_by('-createdAt')[1:4]

    accidents_news_1 = News.objects.filter(category__name="Происшествия").order_by('-createdAt')[:1]
    accidents_news_others = News.objects.filter(category__name="Происшествия").order_by('-createdAt')[1:4]

    sports_news_1 = News.objects.filter(category__name="Спорт").order_by('-createdAt')[:1]
    sports_news_others = News.objects.filter(category__name="Спорт").order_by('-createdAt')[1:4]


    context = {
        'popularity_level_1_news': popularity_level_1_news,
        'popularity_level_2_news': popularity_level_2_news,
        'news': news,

        'show_business_news': show_business_news,

        'economics_news_1': economics_news_1,
        'economics_news_others': economics_news_others,
        
        'society_news': society_news,

        'world_news': world_news,

        'politics_news_1': politics_news_1,
        'politics_news_others': politics_news_others,

        'accidents_news_1': accidents_news_1,
        'accidents_news_others': accidents_news_others,

        'sports_news_1': sports_news_1,
        'sports_news_others': sports_news_others,
    }
    
    return render(request, 'index.html', context)


@api_view(["GET"])
@permission_classes([AllowAny])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def getNews(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def getTheMostPopularNews(request):
    # news = News.objects.filter(popularity_level=1).order_by('-createdAt')[:1]
    news = News.objects.filter(popularity_level=2).order_by('-createdAt')[:6]
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)
