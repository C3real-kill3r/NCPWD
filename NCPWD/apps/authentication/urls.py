from django.urls import path

from .views import (
    LoginAPIView,
    RegistrationAPIView,
    AccountVerificationView)

app_name = "authentication"

urlpatterns = [
    path(
        'users/', RegistrationAPIView.as_view(), name="user-register"),
    path('users/login/', LoginAPIView.as_view(), name="user-login"),
    path(
        'account/verify/<str:token>/<str:uid>/',
        AccountVerificationView.as_view(), name='activate-account'),
]
