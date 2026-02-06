from rest_framework import serializers
from game.models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id', 'title', 'tutorial_url', 'image_path', 'description',
                  'published')
