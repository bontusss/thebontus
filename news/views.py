from django.http.response import Http404
from .africa import scrape_africa
from django.db.models import Q

from news.entertainment import scrape_entertainment
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


class AllStories(APIView):
    """ Displays all the headlines in the database in a reverse order """

    def get(self, request, format=None):
        story = Story.objects.all()[::-1]
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


class NewsFromSource(APIView):
    def get_object(self, source):
        try:
            return Story.objects.filter(newspaper=source)
        except Story.DoesNotExist:
            raise Http404

    def get(self, request, source, format=None):
        story = self.get_object(source)
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)


# search view
class GlobalSearchList(APIView):
    def get_object(self, query_string):
        try:
            return Story.objects.filter(Q(title__icontains=query_string) | Q(url__icontains=query_string) | Q(newspaper__icontains=query_string))
        except Story.DoesNotExist:
            raise Http404

    def get(self, request, query_string, format=None):
        story = self.get_object(query_string)
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)


def scrape(request):
    scrape_business()
    scrape_crypto()
    scrape_newspapers()
    scrape_tech()
    scrape_sports()
    scrape_entertainment()
    scrape_africa()
    return render(request, "news/base.html")
