from django.shortcuts import render
from video_gallery.models import Video
# Create your views here.
def videos(request):
    videos = Video.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'video_gallery/videos.html', context)