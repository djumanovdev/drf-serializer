from rest_framework import serializers
from .models import Category, Task, User
from django.utils import timezone


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    cartegory = CategorySerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'status', 'due_date', 'updated_at', 'created_at', 'cartegory', 'user']
    
    # field level
    def validate_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError({'due_date': 'hozirgi vaqtdan keyingisini tanlang.'})
        return value

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password2': 'password bilan togri emas.'})
        return super().validate(attrs)
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    