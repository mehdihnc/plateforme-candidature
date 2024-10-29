 from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
    path('accounts/', include('accounts.urls')),
    path('home/', include('utilisateurs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
