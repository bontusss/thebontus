from django.urls import path
from .views import AllBusinessNews, AllCryptoNews, AllEntertainmentNews, AllNewspapers, AllStories, AllTechNews, AllSportsNews, GlobalSearchList, NewsFromSource, World, scrape

app_name = 'news'

urlpatterns = [
    path('crypto/', AllCryptoNews.as_view()),
    path('entertainment/', AllEntertainmentNews.as_view()),
    path('tech/', AllTechNews.as_view()),
    path('sports/', AllSportsNews.as_view()),
    path('newspapers/', AllNewspapers.as_view()),
    path('business/', AllBusinessNews.as_view()),
    path('world/', World.as_view()),
    path('all/', AllStories.as_view()),

    # path for different sources
    path('source/<slug:source>/', NewsFromSource.as_view()),

    # global search
    path('search/<slug:query_string>/', GlobalSearchList.as_view()),

    # scraper
    path("scrape/", scrape)


]
