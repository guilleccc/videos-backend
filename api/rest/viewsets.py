'''
@author: gconstantino
'''

from rest_framework import viewsets
from api.rest.serializers.category_seriazer import CategorySerializer
from api.rest.serializers.video_seriazer import VideoSerializer
from api.rest.permissions import AllowAnyOnCreation
from api import models

 

class CategoryViewSet(AllowAnyOnCreation, viewsets.ReadOnlyModelViewSet):
    """ A view set that allows to display all the available categories """
    queryset = models.Category.objects.filter(enabled=True)
    serializer_class = CategorySerializer


class VideoViewSet(AllowAnyOnCreation, viewsets.ReadOnlyModelViewSet):
    """ A view set that allows to display all the videos """
    queryset = models.Video.objects.all()
    serializer_class = VideoSerializer


