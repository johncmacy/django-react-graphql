from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .resources import (
    thing
)



router = DefaultRouter()

router.register('things', thing.ThingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
