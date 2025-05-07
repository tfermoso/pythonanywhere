from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .models import Proyecto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth import logout
from django.conf import settings
from .models import Proyecto  

def index(request):
    proyectos = Proyecto.objects.all().order_by('-id')  # O por el campo que prefieras
    return render(request, "app1/index.html", {"proyectos": proyectos})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Al guardar con UserCreationForm, is_staff y is_superuser quedan a False por defecto
            form.save()
            return redirect('login')  # o donde quieras redirigir tras el registro
    else:
        form = UserCreationForm()
    return render(request, 'app1/register.html', {'form': form})

@login_required
def dashboard(request):
    proyectos = Proyecto.objects.all().order_by('-fecha')  # Puedes filtrar por usuario si lo deseas
    return render(request, 'app1/dashboard.html', {'proyectos': proyectos})


class UserLoginView(LoginView):
    template_name = 'app1/login.html'
    authentication_form = LoginForm
    
class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'app1/proyecto_list.html'    # ruta de tu plantilla
    context_object_name = 'proyectos'            # nombre en el template
    login_url = 'login'                          # nombre de tu url de login
    redirect_field_name = 'next'
    
    
def logout_view(request):
 
    # 2) Destruir completamente la sesión en el servidor
    request.session.flush()
    # 3) Redirigir y borrar la cookie de sesión
    response = redirect('login')
    response.delete_cookie(settings.SESSION_COOKIE_NAME)
    return response# (opcional) query param para volver tras login
