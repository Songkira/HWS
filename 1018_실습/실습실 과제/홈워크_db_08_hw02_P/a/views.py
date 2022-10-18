# 홈워크_db_08_hw02_P-a-1.py
# views.py

from rest_framework import status


@api_view(['GET', 'POST'])
def music_list_create(request):
    if request.method == 'GET':
        musics = Music.objects.all()
        serializer = MusicListSerializer(musics, many=True)
        return Response(serializer.data)
    else:
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid(__(a)__):
            serializer.__(b)__ 
            return Response(serializer.data, status=__(c)__)

(a) => raise_exception=True
(b) => save(article=article)
(c) => status.HTTP_201_CREATE