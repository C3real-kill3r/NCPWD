from django.urls import path, include
from .views import TopicAPIView
from rest_framework import routers


app_name = "topics"

router = routers.DefaultRouter()

router.register(r"topics", TopicAPIView)

urlpatterns = [path('', include(router.urls))]
