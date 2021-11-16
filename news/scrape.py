from .models import Category, Story
from bs4 import BeautifulSoup as BSoup
import requests
import lxml


def scrape_feeds(newspaper_name, link, category):
    session = requests.Session()
    session.headers = {
        "User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"
    }

    url = link

    try:
        content = session.get(url, verify=False).content
        soup = BSoup(content, "xml")
        articles = soup.findAll('item')
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            story = Story()
            story.title = title
            story.url = link
            story.newspaper = newspaper_name
            story.category = Category.objects.get(name=category)
            story.country = 'Nigeria'
            story.save()
            # print(story.url)
            # print(story.title)
            # print(newspaper)
    except Exception as e:
        print(e)
