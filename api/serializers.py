from rest_framework import serializers
from .models import Category, Task
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
