from django.shortcuts import redirect, render
from django.contrib import messages

from crime_app.forms import CrimeForm

# Create your views here.


def home(request):
    # Add a new crime
    if request.method != 'POST':
        # no data is submitted, create a blank form
        form = CrimeForm()
    else:
        # post data submitted, process data
        form = CrimeForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info('Your post has been created.')
            return redirect('crime:home')
    # create an empty form
    context = {'form': form}
    return render(request, 'crimeapp/base.html', context)


def add_crime(request):
    pass
