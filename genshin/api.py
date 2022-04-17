from .serializers import UserSerializer, CharacterSerializer
from rest_framework import viewsets, generics
from .models import User, Character



class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class CharacterView(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all().order_by('name')