from django.utils.text import slugify
from rest_framework import serializers


from .models import Game

class GameSerializer(serializers.ModelSerializer):

    def validate(self, data):
        data['slug'] = slugify(data['name'])
        return data

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = 'id', 'created_at'
