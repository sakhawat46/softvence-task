from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
    UserLogoutView
)

urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name='user-signup'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]