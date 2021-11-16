from django.urls import path

from crime_app.views import add_crime, home

app_name = 'crime_app'

urlpatterns = [
    path('', home, name='home'),
    path('add_crime', add_crime, name='add-crime')
]
