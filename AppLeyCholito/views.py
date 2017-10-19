from django.shortcuts import render
from django.shortcuts import redirect
from .forms import DenunciaForm
from .forms import AuthenticationForm
from .forms import LoginForm
from .models import Denuncia
from django.shortcuts import render, get_object_or_404
<<<<<<< HEAD
#from django.contrib.auth.form import UserCreationForm
=======
from django.contrib.auth.forms import UserCreationForm
>>>>>>> c595d5f54b640e1ecf3e9d398c24816e78d63d35

def index(request):
    return render(request, 'index.html')

def denuncia_new(request):
    if request.method == "POST":
        form = DenunciaForm(request.POST)
        if form.is_valid():
            denucia = form.save()
            return redirect('denuncia_detail', pk=denucia.pk)
    else:
        form = DenunciaForm()
    return render(request, 'denuncia_edit.html', {'form': form})

def authentication(request):
    form = AuthenticationForm
    return render(request, 'authentication.html', {'form': form})

def login(request):
    form = LoginForm
    return render(request, 'login.html', {'form': form})

def denuncia_detail(request, pk):
    denuncia = get_object_or_404(Denuncia, pk=pk)
    return render(request, 'denuncia_detail.html', {'denuncia': denuncia})


#def register(request):
 #   if request.method == 'POST':
 #       form = UserCreationForm(request.POST)
 #       if form.is_valid():
 #           form.save()
 #           return redirect('../')
 #   else:
  #      form = UserCreationForm()
#
 #       args = {'form': form}
  #      return render(request, 'authentication.html', args)