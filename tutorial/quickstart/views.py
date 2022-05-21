from django.contrib.auth.models import User, Group
from rest_framework import serializers, views, viewsets, permissions
from rest_framework.decorators import permission_classes
from quickstart.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows user to bne
  """
  queryset = User.objects.all().order_by('date_joined')
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]
  
class GroupViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited
  """
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  permission_classes = [permissions.IsAuthenticated]
