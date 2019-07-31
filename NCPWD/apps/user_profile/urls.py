from django.urls import path
from .views import ProfileListView, ProfileGetView, DisabilityViewSet

app_name = "user_profile"

urlpatterns = [
    path('', ProfileListView.as_view(), name='get-profiles'),
    path('<str:username>/', ProfileGetView.as_view(), name='profiles'),
    path(r"disability", DisabilityViewSet),
    ]
