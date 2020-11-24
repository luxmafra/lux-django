from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, title, vimeo_id):
        self.slug = slug
        self.title = title
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
       Video('gladiator', 'Video: Gladiator', 482717685),
       Video('spartan', 'Video: Spartan', 483019695),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
