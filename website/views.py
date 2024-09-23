from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PasswordOnlyAuthenticationForm

def custom_login_view(request):
    if request.method == "POST":
        form = PasswordOnlyAuthenticationForm(request.POST)
        if form.is_valid():
            # Get the authenticated user
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('homepage')  # Redirect to a success page
    else:
        if request.user.is_authenticated:
            return redirect('homepage')

        form = PasswordOnlyAuthenticationForm()
    
    return render(request, 'website/login2.html', {'form': form})


def homepage_view(request):
    if request.user.is_authenticated:
        # If user is authenticated, display their username or any other attribute
        username = request.user.username if hasattr(request.user, 'username') else 'No username set'
        return HttpResponse(f"Welcome to the homepage, {username}!")
    else:
        # If user is not authenticated, display a generic message
        return HttpResponse("Welcome to the homepage! Please log in.")