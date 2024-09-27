"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World!")

from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("UNICAS API")

urlpatterns = [
    path('', hello_world, name='hello_world'),  # Add this line
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('juntas.urls')),
    path('', include('prestamos.urls')),
    path('', include('multas.urls')),
    path('', include('acciones.urls')),
    path('', include('agenda.urls')),
    path('', include('capital.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)