'''
@author: gconstantino
'''

#####
from rest_framework import routers

from api.rest import viewsets

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'category', viewsets.CategoryViewSet)

router.register(r'video', viewsets.VideoViewSet)
