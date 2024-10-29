from django.contrib import admin
from .models import JobOffer, Application

@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'applied_at']
    list_filter = ['applied_at']
    search_fields = ['user__username', 'job__title']
