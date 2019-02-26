'''
@author: gconstantino
'''

from rest_framework.permissions import AllowAny, IsAuthenticated


class AllowAnyOnCreation(object):
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

