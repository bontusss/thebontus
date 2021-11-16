from django.forms import ModelForm, Textarea, TextInput
from .models import Crime


class CrimeForm(ModelForm):
    class Meta:
        model = Crime
        fields = ('title', 'report', 'state', 'city',
                  'ongoing', 'longitude', 'latitude')
        widgets = {
            'title': TextInput(attrs={
                "placeholder": 'Title of the crime. eg: Robbery at Abia',
                "class": "form-control form-control-lg shadow-none, border-0"
            }),
            'report': Textarea(attrs={
                "class": "form-control form-control-lg shadow-none, border-0 mt-3",
                "rows": '3',
                "placeholder": 'Write an eye witness report'

            }),
            'state': TextInput(attrs={
                "placeholder": 'State',
                "class": "form-control shadow-none, border-0"
            }),
            'city': TextInput(attrs={
                "placeholder": 'City',
                "class": "form-control shadow-none, border-0"
            }),
            'longitude': TextInput(attrs={
                "placeholder": 'Longitude',
                "class": "form-control shadow-none, border-0"
            }),
            'latitude': TextInput(attrs={
                "placeholder": 'Latitude',
                "class": "form-control shadow-none, border-0"
            }),
        }
