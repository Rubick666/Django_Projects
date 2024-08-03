from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from .models import Event  # Import the Event model from your app

def countdown_timer(request):
    event = Event.objects.first()  # Retrieve the first Event object
    if event:
        time_remaining = event.event_date - timezone.now()  # Calculate time remaining
        hours = time_remaining.seconds // 3600
        minutes = (time_remaining.seconds % 3600) // 60
        seconds = time_remaining.seconds % 60
        data = {
            'name': event.name,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }
    else:
        data = {
            'name': "No Event",
            'hours': 0,
            'minutes': 0,
            'seconds': 0
        }
    return render(request, 'myapp.html', {'data': data})
