from django.urls import path
from .views import (
    ProfileListView, ProfileGetView, DisabilityViewSet, MyProfile)

app_name = "user_profile"

urlpatterns = [
    path('', ProfileListView.as_view(), name='get-profiles'),
    path('mine/', MyProfile.as_view(), name='my-profile'),
    path('<str:username>/', ProfileGetView.as_view(), name='profiles'),
    path(r"disability", DisabilityViewSet),
    ]
