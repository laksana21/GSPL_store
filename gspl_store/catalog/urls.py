# Django library
from django.urls import include, path

# Django Rest Framework library
from rest_framework import routers

# Project library
from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', views.login),
    path('auth/logout/', views.logout)
]
