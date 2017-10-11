from django.shortcuts import render
from django.shortcuts import redirect
from .forms import DenunciaForm
from .forms import AuthenticationForm
from .forms import LoginForm

def denuncia_new(request):
    if request.method== "POST":
        form = DenunciaForm(request.POST)
        if form.is_valid():
            denucia= form.save()
    else:
        form = DenunciaForm()
    return render(request, 'denuncia_edit.html', {'form': form})

def authentication(request):
    form = AuthenticationForm
    return render(request, 'authentication.html', {'form': form})

def login(request):
    form = LoginForm
    return render(request, 'login.html', {'form': form})

