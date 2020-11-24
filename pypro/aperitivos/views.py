from django.shortcuts import render


def video(request, slug):
    video = {'title': 'Video: Gladiator', 'vimeo_id': 482717685}
    return render(request, 'aperitivos/video.html', context={'video': video})
