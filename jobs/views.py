from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import JobOffer, Application
from .forms import ApplicationForm

def job_list(request):
    """
    Affiche la liste des offres d'emploi actives.
    Accessible à tous les utilisateurs.
    """
    jobs = JobOffer.objects.filter(is_active=True)
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(JobOffer, pk=pk)
    has_applied = Application.objects.filter(user=request.user, job=job).exists() if request.user.is_authenticated else False
    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'has_applied': has_applied
    })

@login_required
def apply_job(request, pk):
    """
    Permet à un utilisateur connecté de postuler à une offre.
    Vérifie si l'utilisateur n'a pas déjà postulé.
    """
    job = get_object_or_404(JobOffer, pk=pk)
    if Application.objects.filter(user=request.user, job=job).exists():
        messages.warning(request, 'Vous avez déjà postulé à cette offre.')
        return redirect('job_detail', pk=pk)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()
            messages.success(request, 'Candidature envoyée avec succès!')
            return redirect('job_list')
    else:
        form = ApplicationForm()
    
    return render(request, 'jobs/apply.html', {'form': form, 'job': job})
