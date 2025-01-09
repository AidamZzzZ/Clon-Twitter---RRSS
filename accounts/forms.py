from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = Profile
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'photo']

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = Profile
		fields = ['photo', 'bio']

