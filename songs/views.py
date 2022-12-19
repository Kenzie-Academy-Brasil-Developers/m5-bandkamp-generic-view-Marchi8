from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from rest_framework.generics import ListCreateAPIView
from django.shortcuts import get_object_or_404
from albums.models import Album


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        album = get_object_or_404(Album, id=self.kwargs["pk"])
        serializer.save(album_id=album.id)

    def get_queryset(self):
        album = get_object_or_404(Album, id=self.kwargs["pk"])
        return self.queryset.filter(album_id=album.id)
