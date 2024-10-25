from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ProfilCandidat

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'utilisateurs/login.html')

@login_required
def profile_view(request):
    profil = ProfilCandidat.objects.get(utilisateur=request.user)
    if request.method == 'POST':
        
        profil.cv = request.FILES.get('cv')
        profil.save()
    return render(request, 'utilisateurs/profile.html', {'profil': profil})