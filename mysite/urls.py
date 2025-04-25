"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from app1 import views   # Importar las vistas de app1
from django.contrib.auth.views import LogoutView
from app1.views import UserLoginView
from django.conf import settings
from django.conf.urls.static import static
from app1.views import ProyectoListView

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    # Página de login
    path('login/', UserLoginView.as_view(), name='login'),
    # (Opcional) Logout redirigiendo a home
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/', include('api.urls')),
    path('salir/', views.logout_view, name='salir'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

