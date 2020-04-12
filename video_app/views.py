from django.shortcuts import render
from .models import videos
# Create your views here.
def video(request):

    video = videos.objects.all()

    content = {
        'videos':video,
    }

    return render(request, 'video.html', content)
