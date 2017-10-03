from django.shortcuts import render
from .forms import DenunciaForm

def denuncia_new(request):
    form= DenunciaForm
    return render(request, 'denuncia_edit.html', {'form': form})

