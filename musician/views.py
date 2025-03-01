from rest_framework import viewsets

from musician.models import Musician
from musician.serializers import (
    MusicianListSerializer,
    MusicianSerializer,
    MusicianRetrieveSerializer,
)


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MusicianListSerializer
        elif self.action == "retrieve":
            return MusicianRetrieveSerializer

        return MusicianSerializer
