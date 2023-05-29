from celery.app import routes
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    UserLoginView,
    UserRegistrationView,
    UserProfileView,
    UserLogoutView
)
router = DefaultRouter()
router.register(r'user', UserProfileView)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]
urlpatterns += router.urls