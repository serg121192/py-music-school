from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.BooleanField(read_only=True)

    class Meta:
        model = Musician
        fields = (
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult"
        )


class MusicianListSerializer(MusicianSerializer):
    pass


class MusicianRetrieveSerializer(MusicianSerializer):
    pass
