from rest_framework import serializers
from .models import *
  
class WordCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataStore
        fields = ('id', 'url', 'word_count', 'favourite', 'web_links', 'media_links')