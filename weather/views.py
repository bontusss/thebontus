from django.shortcuts import render
from .config import KEY
import requests
# Create your views here.
api_key = KEY


def home(request):
    city = 'Abia'
    # url = f'api.openweathermap.org/data/2.5/weather?q={city},{state_code},{country_code}&appid={API key}'
    url = f'api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    data = requests.get(url).json()
    print(data)
    weather = {
        "city": city,
        "temperature": data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }
    return render(request, "weather/base.html")
