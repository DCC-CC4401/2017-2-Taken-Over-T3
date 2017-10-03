from django import forms
from .models import Denuncia

TIPOS_SEXO=(('H',"Hembra"),('M',"Macho"))

class DenunciaForm(forms.ModelForm):
    Herido = forms.BooleanField()
    Sexo = forms.MultipleChoiceField(required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=TIPOS_SEXO,
    )
    class Meta:
        model= Denuncia
        fields = ('TipDenucia', 'Animal','Sexo','Herido','Color','Comentario')
