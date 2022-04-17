from rest_framework import serializers
from .models import User, Character 
from rest_framework.permissions import IsAdminUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class CharacterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Character
        fields = ('__all__')
        permission_classes = [IsAdminUser,]
    