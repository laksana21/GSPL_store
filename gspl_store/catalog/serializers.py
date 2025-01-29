# Django library
from django.contrib.auth.models import Group, User
from django.utils import timezone

# Django Rest Framework library
from rest_framework import serializers

# Project library
from .models import Product

# User Management
class UserSerializer(serializers.Serializer):
  class Meta:
      model = User
      fields = ['url', 'username', 'password', 'email', 'groups']


class GroupSerializer(serializers.Serializer):
  class Meta:
    model = Group
    fields = ['url', 'name']

# Product Management
class ProductSerializer(serializers.Serializer):
  # Product Serialization
  Id = serializers.IntegerField(read_only=True)
  name = serializers.CharField(required=True)
  description = serializers.CharField(required=True)
  price = serializers.DecimalField(max_digits=20, decimal_places=2)
  created_at = serializers.DateTimeField(read_only=True)
  updated_at = serializers.DateTimeField(read_only=True)

  def create(self, data):
    return Product.objects.create(**data)
  
  def update(self, instance, data):
    instance.name = data.get('name', instance.name)
    instance.description = data.get('description', instance.description)
    instance.price = data.get('price', instance.price)
    instance.updated_at = timezone.now()

    instance.save()
    return instance
