from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Profile

# Create your views here.
class UserRegisterView(CreateView):
	form_class = CustomUserCreationForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

class UserUpdateView(UpdateView):
	form_class = CustomUserChangeForm
	template_name = 'registration/user_change_form.html'
	success_url = reverse_lazy('profile')

	def get_queryset(self):
		return Profile.objects.filter(username=self.request.user)

@login_required
def home(request):
	user_instance = request.user
	profiles_instances = Profile.objects.all().exclude(id=user_instance.id)

	context = {
		'profiles': profiles_instances
	}

	return render(request, 'home.html', context)

@login_required
def profile_view(request):
	user_instance = request.user.pk
	profile_instance = get_object_or_404(Profile, pk=user_instance)

	context = {
		'profile': profile_instance
	}

	return render(request, 'accounts/profile.html', context)

@login_required
def detail_user(request, pk):
	profile_instance = get_object_or_404(Profile, pk=pk)

	if request.method == 'POST':

		current_user_profile = request.user	
		action = request.POST.get('follow', 'unfollow')

		if action == 'unfollow':
			current_user_profile.follows.remove(profile_instance)

		elif action == 'follow':
			current_user_profile.follows.add(profile_instance)

		current_user_profile.save()

	context = {
		'user_detail': profile_instance,
	}

	return render(request, 'accounts/detail_user.html', context)
