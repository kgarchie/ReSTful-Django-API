from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'story', 'headline', 'writer', 'photographer', 'date_time', 'date']
