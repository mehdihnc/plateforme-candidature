# utilisateurs/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    HomeView,
    CandidateRegisterView,
    RecruiterRegisterView,
    CustomLoginView,
    CandidateProfileView,
    RecruiterDashboardView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/candidate/', CandidateRegisterView.as_view(), name='candidate_register'),
    path('register/recruiter/', RecruiterRegisterView.as_view(), name='recruiter_register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/candidate/', CandidateProfileView.as_view(), name='candidate_profile'),
    path('dashboard/recruiter/', RecruiterDashboardView.as_view(template_name="recruiter_dashboard.html"), name='recruiter_dashboard'),
]
