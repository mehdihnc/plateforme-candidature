from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'cv')
    search_fields = ('user__username', 'user_type')
    list_filter = ('user_type',)

admin.site.register(UserProfile, UserProfileAdmin)