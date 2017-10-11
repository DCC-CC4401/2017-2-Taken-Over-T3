#from django.htpp import Http404
from django.shortcuts import render
from .forms import DenunciaForm
from .forms import AuthenticationForm
from .forms import LoginForm
#from django.http import HttpResponse
from .models import Login


def index(request):
    return render(request, 'index.html')

def landing_page(request):
    all_users = Login.objects.all()
    context = {'all_users': all_users}
    #return HttpResponse("<h1>Landing Page</h1>")
    return render(request, 'AppLeyCholito/landing_page.html', context)


def denuncia_new(request):
    form = DenunciaForm
    return render(request, 'denuncia_edit.html', {'form': form})

def authentication(request):
    form = AuthenticationForm
    return render(request, 'authentication.html', {'form': form})

def login(request):
    form = LoginForm
    return render(request, 'login.html', {'form': form})
    #return render(request, 'login.html')


#Al hacer login con un usuario incorrecto?

#def detail(request, user_name):
 #   try:
  #      user = Login.objects.get(username=user_name)
   # except Login.DoesNotExist:
    #    raise Http404("Usuario no existe")
    #return render(request, 'login.html')

