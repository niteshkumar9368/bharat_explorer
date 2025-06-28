# core/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

class LogoutGetAllowedView(auth_views.LogoutView):
    # Allow GET requests for logout (less secure)
    http_method_names = ['get', 'post']

urlpatterns = [
    path('admin/', admin.site.urls),

    # App-level routing
    path('', include(('places.urls', 'places'), namespace='places')),

    # Include accounts app URLs for registration
    path('accounts/', include('accounts.urls')),

    # Auth routes
    path('login/', auth_views.LoginView.as_view(template_name='places/login.html'), name='login'),
    path('logout/', csrf_exempt(LogoutGetAllowedView.as_view(next_page='login')), name='logout'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
