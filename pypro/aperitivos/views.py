from django.shortcuts import render

videos = [
       {'slug': 'gladiator', 'title': 'Video: Gladiator', 'vimeo_id': 482717685},
       {'slug': 'spartan', 'title': 'Video: Spartan', 'vimeo_id': 482717685},
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
