'''

@author: gconstantino
'''
from rest_framework import serializers
from api import models


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """
    It is the basic representation of the Category model
    """
    class Meta:
        model = models.Category
        fields = ('url', 'id', 'slug', 'name', 'enabled', 'main_category')

