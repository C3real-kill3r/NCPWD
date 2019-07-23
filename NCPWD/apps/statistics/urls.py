from django.urls import path
from .views import StatisticsViews


urlpatterns = [path('statistics', StatisticsViews.as_view(), name="statistics")]

