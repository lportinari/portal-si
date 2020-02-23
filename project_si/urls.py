"""project_si URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('santacruz_homolog/', include('santacruz_homolog.urls', namespace='santacruz_homolog')),
    path('panpharma_homolog/', include('panpharma_homolog.urls', namespace='panpharma_homolog')),
    path('santacruz_producao/', include('santacruz_producao.urls', namespace='santacruz_producao')),
    path('panpharma_producao/', include('panpharma_producao.urls', namespace='panpharma_producao')),
]
