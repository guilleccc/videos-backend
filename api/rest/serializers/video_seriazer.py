'''

@author: gconstantino
'''
from rest_framework import serializers
from api import models


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    """
    It is the basic representation of the Video model
    """
    class Meta:
        model = models.Video
        fields = ('url', 'id', 'category', 'name', 'video', 'thumbs_up', 'thumbs_down')

