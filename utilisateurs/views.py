from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView

from utilisateurs.forms import UserRegistrationForm
from .models import UserProfile
from django.urls import reverse_lazy
from django import forms

class HomeView(TemplateView):
    template_name = 'utilisateurs/home.html'

class CandidateRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'utilisateurs/register.html'
    success_url = reverse_lazy('candidate_profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object, user_type='candidate')
        return response


class RecruiterRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'utilisateurs/register.html'
    success_url = reverse_lazy('recruiter_dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object, user_type='recruiter')
        return response
    
class CustomLoginView(LoginView):
    template_name = 'utilisateurs/login.html'

    def get_success_url(self):
        user_profile = UserProfile.objects.get(user=self.request.user)
        if user_profile.user_type == 'candidate':
            return reverse_lazy('candidate_profile')
        elif user_profile.user_type == 'recruiter':
            return reverse_lazy('recruiter_dashboard')
        
class CandidateProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'utilisateurs/candidate_profile.html'

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user, user_type='candidate')

    
class RecruiterDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'utilisateurs/recruiter_dashboard.html'

    def test_func(self):
        return UserProfile.objects.filter(user=self.request.user, user_type='recruiter').exists()