from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer

@api_view(['GET'])
def song_list(request):
    if request.method == 'GET':
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
           serializer.save()
           return Response(serializer.data) 
        else:
            return Response(serializer, status=status.HTTP_201_CREATED)
