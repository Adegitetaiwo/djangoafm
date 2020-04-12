from django.shortcuts import render
from .models import audios
# Create your views here.
def audio(request):
    currentAudio = audios.objects.last()
    previousAudio = audios.objects.all()

    content = {
        'current':currentAudio,
        'previous': previousAudio,
    }
    return render(request, 'audio.html', content)