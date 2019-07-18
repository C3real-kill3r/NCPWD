from django.urls import path

from .views import (
    LoginAPIView,
    RegistrationAPIView,
    AccountVerificationView,
    ForgotPasswordView,
    ResetPasswordView
    )

app_name = "authentication"

urlpatterns = [
    path(
        'users/', RegistrationAPIView.as_view(), name="user-register"),
    path('users/login/', LoginAPIView.as_view(), name="user-login"),
    path(
        'account/verify/<str:token>/<str:uid>/',
        AccountVerificationView.as_view(), name='activate-account'),
    path(
        'password/forgot/',
        ForgotPasswordView.as_view(), name="forgot-password"),
    path(
        'password/reset/<str:token>/',
        ResetPasswordView.as_view(), name="reset-password"),
]
