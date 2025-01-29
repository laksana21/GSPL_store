from django.db import models

# Create your models here.

# Product entity model
class Product(models.Model):
  Id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=20, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['created_at']
