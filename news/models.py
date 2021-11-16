from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


# class Headline(models.Model):
#     """ This contains only headlines from selected newspapers """
#     title = models.CharField(max_length=200)
#     image = models.ImageField(upload_to="uploads/", blank=True, null=True)
#     url = models.URLField()
#     newspaper = models.CharField(
#         max_length=20, help_text='newspaper that owns the headline')
#     datee = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.title


class Category(models.Model):
    """ news category """
    name = models.CharField(max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Story(models.Model):
    """ This contains all kinds of news stories filtered by their category eg: sports, world news"""
    title = models.CharField(max_length=500)
    url = models.URLField(max_length=500)
    newspaper = models.CharField(
        max_length=20, help_text='newspaper that owns the headline')
    datee = models.DateField(auto_now_add=True)
    country = models.CharField(
        max_length=50, help_text="Country where the story is coming from")
    category = models.ForeignKey(
        Category, on_delete=CASCADE, help_text="Eg: Sports, Entertainment")

    def __str__(self):
        return self.title
