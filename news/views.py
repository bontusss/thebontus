from .business import scrape_business
from .newspapers import scrape_newspapers
from .crypto import scrape_crypto
from .tech import scrape_tech
from .sports import scrape_sports
from .serializers import StorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters, generics
from .models import Story, Category
from django.shortcuts import render


# by categories

class AllCryptoNews(APIView):
    """ Displays all the headlines in the database in a reverse order """

    def get(self, request, format=None):
        story = Story.objects.filter(
            category=Category.objects.get(name="Crypto"))[::-1]
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)


class AllNewspapers(APIView):
    """ Displays all the stories from newspaper sources """

    def get(self, request, format=None):
        # scrape_feeds(
        #     "Daily Trust", 'https://dailytrust.com/feed', "Newspaper")
        story = Story.objects.filter(
            category=Category.objects.get(name="Newspaper"))[::-1]
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)


class AllSportsNews(APIView):
    def get(self, request, format=None):
        story = Story.objects.filter(
            category=Category.objects.get(name="Sports"))[::-1]
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)


class AllEntertainmentNews(APIView):
    def get(self, request, format=None):
        story = Story.objects.filter(
            category=Category.objects.get(name="Entertainment"))[::-1]
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)


class AllTechNews(APIView):
    def get(self, request, format=None):
        story = Story.objects.filter(
            category=Category.objects.get(name="Technology"))[::-1]
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)


class AllBusinessNews(APIView):
    def get(self, request, format=None):
        story = Story.objects.filter(
            category=Category.objects.get(name="Business"))[::-1]
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)


class AllBlogs(APIView):
    def get(self, request, format=None):
        story = Story.objects.filter(
            category=Category.objects.get(name="Blogs"))[::-1]
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)


class World(APIView):
    def get(self, request, format=None):
        story = Story.objects.filter(
            category=Category.objects.get(name="World"))[::-1]
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)

# By Newspapers


class NewsFromLeadership(APIView):
    def get(self, request, format=None):
        story = Story.objects.filter(newspaper="Leadership")
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)


class NewsFromPunch(APIView):
    def get(self, request, format=None):
        story = Story.objects.filter(newspaper="Punch")
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)


# search view
# class GlobalSearchList(ListAPIView):
#     serializer_class = StorySerializer

#     def get_queryset(self):
#         query = self.request.QUERY_PARAMS.get('query', None)
#         story = Story.objects.filter(Q(code__icontains=query) | Q(highlighted__icontains=query) | Q(language__icontains=query))
#         category = Category.objects.filter(username__icontains=query)
#         all_results = list(chain(story, category))
#         all_results.sort(key=lambda x: x.created)
#         return all_results


def scrape(request):
    scrape_business()
    scrape_crypto()
    scrape_newspapers()
    scrape_tech()
    scrape_sports()
    return render(request, "news/base.html")
