from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def dashboard(request):
    profile = request.user.userprofile
    if profile.user_type == 'Patient':
        return render(request, 'accounts/patient_dashboard.html', {'profile': profile})
    elif profile.user_type == 'Doctor':
        return render(request, 'accounts/doctor_dashboard.html', {'profile': profile})
