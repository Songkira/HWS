from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http.response import JsonResponse, HttpResponse
from .serializers import MusicSerializer
from django.core import serializers
from .models import Music
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
def music_html(request):
    musics = Music.objects.all()
    context = {
        "musics": musics,
    }
    return render(request, "music/music.html", context)


def music_json_1(request):
    musics = Music.objects.all()
    musics_json = []

    for music in musics:
        musics_json.append(
            {
                "id": music.pk,
                "title": music.title,
                "content": music.content,
                # "created_at": music.created_at,
                # "updated_at": music.updated_at,

            }
        )
    return JsonResponse(musics_json, safe=False)


def music_json_2(request):
    musics = Music.objects.all()
    data = serializers.serialize(
        "json",
        musics,
        fields=(
            "title",
            "content",
            # "created_at",
            # "updated_at",
        ),
    )
    return HttpResponse(data, content_type="application/json")


# def music_json_3(request):
#     musics = Music.objects.all()
#     data = serializers.serialize('json', musics)
#     return HttpResponse(data, content_type='application/json')

@api_view(['GET',])
def music_json_3(request):
    # musics = get_list_or_404(Music)
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)