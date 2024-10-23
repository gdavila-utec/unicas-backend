from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_root(request):
    return JsonResponse({
        "status": "ok",
        "message": "UNICAS API is running"
    })

@csrf_exempt
def health_check(request):
    return JsonResponse({
        "status": "healthy",
        "environment": settings.ENVIRONMENT if hasattr(settings, 'ENVIRONMENT') else 'production'
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/', api_root, name='api-root'),
    path('api/health/', health_check, name='health-check'),
    path('api/', include('users.urls')),
    # Include app URLs
    path('', include('users.urls')),  # This line includes user URLs
    path('', include('juntas.urls')),
    path('', include('prestamos.urls')),
    path('', include('multas.urls')),
    path('', include('acciones.urls')),
    path('', include('agenda.urls')),
    path('', include('capital.urls')),
]

# Static and media files
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)