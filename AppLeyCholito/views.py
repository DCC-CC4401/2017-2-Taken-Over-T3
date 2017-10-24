from django.shortcuts import render, redirect
from .forms import DenunciaForm
from .forms import AnimalForm
from .forms import AuthenticationForm, UserForm
from .forms import LoginForm
from .forms import DenunciaForm1
from .models import Denuncia
from .models import Animal
from django.shortcuts import render, get_object_or_404
#from django.contrib.auth.form import UserCreationForm
from django.views.generic import View
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'index.html')

def denuncia_new(request):
    if request.method == "POST":
        form = DenunciaForm1(request.POST)
        if form.is_valid():
            denucia = form.save(commit=False)
            denucia.Estado_Denuncia = 'reportadas'
            denucia.save()
            return redirect('denuncia_detail', pk=denucia.pk)
    else:
        form = DenunciaForm()
    return render(request, 'denuncia_nueva.html', {'form': form})

def denuncia_detail(request, pk):
    denuncia = get_object_or_404(Denuncia, pk=pk)
    return render(request, 'denuncia_detail.html', {'denuncia': denuncia})

def denuncia_edit(request, pk):
    if request.method == "POST":
        form = DenunciaForm1(request.POST)
        if form.is_valid():
            denuncia = form.save()
            denuncia.save()
            return redirect('denuncia_detail', pk=denuncia.pk)
    else:
        denuncia = get_object_or_404(Denuncia, pk=pk)
        form = DenunciaForm1(instance=denuncia)
        return render(request, 'denuncia_edit.html', {'form': form})

def animal_new(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save()
            animal.save()
            return redirect('animal_detail',pk=animal.pk)
    else:
        form=AnimalForm()
    return  render(request, 'animal_edit.html', {'form': form})



def authentication(request):
    form = AuthenticationForm

    return render(request, 'authentication.html', {'form': form})

class Login(View):
    form_class = LoginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')

        return render(request, 'login.html', {'form': form})


def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'animal_detail.html', {'animal': animal})

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


class UserFormView(View):
    form_class = UserForm
    template_name = 'authentication.html'
    #display blank form (new user)
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data (post)
    def post(self, request):
        form = self.form_class(request.POST)

        #store in database
        if form.is_valid():
            # crea un objeto del formulario, pero no lo guarda en la DB todavia
            user = form.save(commit=False)
            # limpieza (normalizar) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save() #guarda en la DB

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')

                    # request.user.username ##para ver los datos del user
        return render(request, self.template_name, {'form': form})


def municipalidad(request): #pk
    return render(request, 'muni_ong.html') #, {'muni': muni})

def muniOngStats(request): #pk
    return render(request, 'muni_ong_stats.html') #, {'muni': muni})

def muniDenuncias(request):
    denuncias = Denuncia.objects.all()
    return render(request, 'muni_denuncias.html', {'denuncias': denuncias})