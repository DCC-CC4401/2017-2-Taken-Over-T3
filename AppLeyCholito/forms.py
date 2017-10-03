from django import forms
from .models import Denuncia

class DenunciaForm(forms.ModelForm):
    class Meta:
        model= Denuncia
        fields = ('TipDenucia', 'Animal','Sexo','Color','Comentario')
