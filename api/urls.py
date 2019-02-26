'''
Created on Jan 11, 2016

@author: gconstantino
'''
from django.conf.urls import url, include

from api.rest.routers import router
from django.views.generic.base import TemplateView


urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name="videos/home.html"), name='home'),

    url(r'^api/', include(router.urls)),

]
