from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'login_count', 'is_active', 'is_admin', 'is_staff')
        read_only_fields = ('id', 'is_active', 'is_staff')
