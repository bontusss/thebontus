from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.


class Crime(models.Model):
    """ model for a crime """
    title = models.CharField(max_length=50, help_text='Title of the crime')
    report = models.TextField(help_text='Eye witness report')
    state = models.CharField(
        max_length=10, help_text='The state the crime happened')
    city = models.CharField(
        max_length=10, help_text='The city the crime happened')
    ongoing = models.BooleanField(
        default=False, help_text='Is the crime ongoing?')
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
