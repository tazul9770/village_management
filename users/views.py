from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import RegistrationForm, LoginForm, AssignRoleForm, CreateGroupForm
from village.forms import EditProfileForm
from village.models import UserProfile
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

User = get_user_model()

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.is_active = False
            user.save()
            messages.success(request, "A confirmation mail send. Please check your email!")
            return redirect('register')
    return render(request, 'registration/register.html', {'form':form})
    
def log_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html', {'form':form})

def active_user(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect("login")
        else:
            return HttpResponse("Invalid Id or token")
    except User.DoesNotExist:
        return HttpResponse("User not found")

@login_required    
def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required  
def user_profile(request):
    try:
        profile = UserProfile.objects.select_related('user').get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None
    return render(request, "profile/profile.html", {'profile':profile})


@login_required
def profile_edit(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    form = EditProfileForm(instance=profile, user=request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile update done!")
            return redirect('profile_edit')
    return render(request, "profile/edit_profile.html", {'form':form})

def assign_role(request, user_id):
    user = User.objects.get(id=user_id)
    form = AssignRoleForm()
    if request.method == 'POST':
        form = AssignRoleForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get('role')
            user.groups.clear()
            user.groups.add(role)
            messages.success(request, f"You assigned to {role.name}")
            return redirect('admin_dashboard')
    return render(request, 'registration/assign_role.html', {'form':form})

def create_group(request):
    form = CreateGroupForm()
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Group created successfully !")
            return redirect('admin_dashboard')
    return render(request, "registration/create_group.html", {'form':form})

def show_group(request):
    groups = Group.objects.all()
    return render(request, 'profile/show_group.html', {'groups':groups})
    