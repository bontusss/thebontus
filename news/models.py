from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Category(models.Model):
    """ news category """
    name = models.CharField(max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Story(models.Model):
    """ This contains all kinds of news stories filtered by their category eg: sports, world news"""
    title = models.CharField(max_length=500, unique=True)
    url = models.URLField(max_length=500, unique=True)
    newspaper = models.CharField(
        max_length=20, help_text='newspaper that owns the headline')
    datee = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, help_text="Eg: Sports, Entertainment")

    def __str__(self):
        return self.title

    def get_category_url(self):
        return f'/{self.category.slug}'
