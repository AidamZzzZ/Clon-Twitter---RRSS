from django.urls import path
from .views import (
	home, 
	UserRegisterView,
	UserUpdateView,
	profile_view, 
	detail_user
)

urlpatterns = [
	path('user_profile/', profile_view, name="profile"),
	path('profile/<int:pk>', detail_user, name="user_detail"),
	path('register/', UserRegisterView.as_view(), name="register"),
	path('user-change/<int:pk>', UserUpdateView.as_view(), name="user_change"),
]