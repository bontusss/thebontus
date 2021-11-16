from rest_framework import serializers

from .models import Story


class StorySerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")

    class Meta:
        model = Story
        fields = [
            "id",
            "title",
            "url",
            "newspaper",
            'datee',
            'country',
            "category",
        ]
