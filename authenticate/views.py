from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

def home(request):
	if request.user.is_authenticated:
		return redirect('snippet_detail')
	else:
		return render(request, 'authenticate/home.html')

def returning_profile_home(request):
	return render(request, 'authenticate/returning_profile_home.html', {})

def new_profile_home(request):
	return render(request, 'authenticate/new_profile_home.html', {})

def login_user(request):
	if request.method =='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('You have been logged in'))
			return redirect('snippet_detail')

		else:
			messages.success(request, ('Error logging in - Please try again...'))
			return redirect('login')

	else:
		return render(request, 'authenticate/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ('You have been logged out'))
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ('You have registered...'))
			return redirect('new_profile_home')

	else:
		form = SignUpForm()

	context = {'form': form}
	return render(request, 'authenticate/register.html', context)

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You have edited your profile...'))
			return redirect('returning_profile_home')

	else:
		form = EditProfileForm(instance=request.user)

	context = {'form': form}
	return render(request, 'authenticate/edit_profile.html', context)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You have edited your password...'))
			return redirect('home')

	else:
		form = PasswordChangeForm(user=request.user)

	context = {'form': form}
	return render(request, 'authenticate/change_password.html', context)

#create view
def sentence_collect_page(request):
	if request.method == "POST":
		form = SentenceForm(data=request.POST, instance=request.user )
		if form.is_valid():
			form.save()
			messages.success(request, ('We have saved your sentence!'))
			return redirect('sentence_collect_page')

	else:
		form = SentenceForm(instance=request.user)

	context = {'form': form}
	return render(request, 'authenticate/sentence_collect_page.html', context)

#list view
