from django import template
from django.utils import timezone

register = template.Library()


def current_date():
    date = timezone.now()
    return date
