#from django.shortcuts import render
# standard library
import re
import decimal

# Django library
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate

# Django Rest Framework library
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

# Project library
from .serializers import ProductSerializer
from .models import Product

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Product to be added, viewed, edited, or deleted.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    page_size = 10

    # Get all product function
    def list(self, request):
      products = Product.objects.all()
      
      name = request.GET.get('name', None)
      price = request.GET.get('price', None)
      price_min = request.GET.get('price_min', None)
      price_max = request.GET.get('price_max', None)
      page_args = request.GET.get('page_size', None)
      
      paginator = PageNumberPagination()

      if page_args and int(page_args) > 0:
        paginator.page_size = int(page_args)
      else:
        paginator.page_size = ProductViewSet.page_size

      if name:
        products = products.filter(name__icontains=name)
      if price_min and price_max:
        products = products.filter(price__gte=price_min, price__lte=price_max)
      if price:
        products = products.filter(price=price)

      result_page = paginator.paginate_queryset(products, request)
      serializer = ProductSerializer(result_page, many=True)

      return paginator.get_paginated_response(serializer.data)
    
    # Add new product function
    def create(self, request):
      if request.user.is_authenticated:
        data = JSONParser().parse(request)
        price_temp = data["price"].lower()

        if "idr" in price_temp:
          price_strip = re.sub('[^\d\.]', '', price_temp)
          price_data = decimal.Decimal(price_strip) / decimal.Decimal(10000)
        else:
          price_strip = re.sub('[^\d\.]', '', price_temp)
          price_data = decimal.Decimal(price_strip)

        data["price"] = price_data
        serializer = ProductSerializer(data=data)

        if serializer.is_valid():
          serializer.save()
          return Response({'Success': 'Product added'}, status=200)
        else:
          return Response(serializer.errors, status=400)
      else:
        return Response({'error': 'Invalid credentials'}, status=401)

    # Get detail product function
    def retrieve(self, request, pk):
      try:
        product = Product.objects.get(pk=pk)
      except Product.DoesNotExist:
        return Response({'error': 'Product is not found'}, status=404)

      serializer = ProductSerializer(product)

      return Response(serializer.data)

    # Update product function
    def update(self, request, pk):
      if request.user.is_authenticated:
        data = JSONParser().parse(request)
        price_temp = data["price"].lower()

        if "idr" in price_temp:
          price_strip = re.sub('[^\d\.]', '', price_temp)
          price_data = decimal.Decimal(price_strip) / decimal.Decimal(10000)
        else:
          price_strip = re.sub('[^\d\.]', '', price_temp)
          price_data = decimal.Decimal(price_strip)

        data["price"] = price_data

        try:
          product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
          return Response({'error': 'Product is not found'}, status=404)
        
        serializer = ProductSerializer(product, data=data)

        if serializer.is_valid():
          serializer.save()
          return Response({'Success': 'Product updated'}, status=200)
        else:
          return Response(serializer.errors, status=400)
      else:
        return Response({'error': 'Invalid credentials'}, status=401)

    # Delete product function
    def destroy(self, request, pk):
      if request.user.is_authenticated:
        try:
          product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
          return Response({'error': 'Product is not found'}, status=404)
        
        product.delete()
        return Response({'success': 'Product deleted'}, status=200)
      else:
        return Response({'error': 'Invalid credentials'}, status=401)
    
# Authentication Section
@api_view(('POST',))
def login(request):
  """
  API endpoint that allows User to get access token.
  """
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request, username=username, password=password)
  if user:
    token, created = Token.objects.get_or_create(user=user)
    return Response({
      'access_token': token.key,
      "expires_in": 3600,
      "token_type": "Bearer"
    })
  else:
    return Response({'error': 'Invalid credentials'}, status=401)
  
@api_view(('POST',))
def logout(request):
  """
  API endpoint that allows User to remove access token.
  """
  try:
    request.user.auth_token.delete()
  except (AttributeError, ObjectDoesNotExist):
    pass

  return Response({"success": "Successfully logged out."}, status=200)
