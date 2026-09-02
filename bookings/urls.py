from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import BookingCreateView, ContactMessageCreateView, MeView, RegisterView

urlpatterns = [
    path("bookings/", BookingCreateView.as_view(), name="booking-create"),
    path("messages/", ContactMessageCreateView.as_view(), name="message-create"),
    path("auth/register/", RegisterView.as_view(), name="auth-register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="auth-login"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="auth-refresh"),
    path("auth/me/", MeView.as_view(), name="auth-me"),
]
