from django.urls import path
from .views import AllBusinessNews, AllCryptoNews, AllEntertainmentNews, AllNewspapers, AllTechNews, AllSportsNews, NewsFromLeadership, NewsFromPunch, World, scrape

app_name = 'news'

urlpatterns = [
    path('crypto/', AllCryptoNews.as_view()),
    path('entertainment/', AllEntertainmentNews.as_view()),
    path('tech/', AllTechNews.as_view()),
    path('sports/', AllSportsNews.as_view()),
    path('newspapers/', AllNewspapers.as_view()),
    path('business/', AllBusinessNews.as_view()),
    path('world/', World.as_view()),

    # path for different sources
    path('leadership/', NewsFromLeadership.as_view()),
    path('punch/', NewsFromPunch.as_view()),

    # global search
    # path('search/', GlobalSearchList.as_view())

    # scraper
    path("scrape/", scrape)


]
