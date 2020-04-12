from django.shortcuts import render
from .models import liveForcast
# Create your views here.
def live_forcast(request):

    live_forcast = liveForcast.objects.last()
    content = {
        'live':live_forcast,
    }
    return render(request, 'live-forcast.html', content)