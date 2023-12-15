
from django import forms
from django.core.exceptions import ValidationError
from . import models

#formulario
class ContactForm(forms.ModelForm): #baseado no model que eu ja tenho
    
    first_name = forms.CharField(
        widget=forms.TextInput( #outra forma de adicionar widget mexendo no campo inteiro - como foi feito no model
            attrs= {
                'placeholder':'Seu nome'
            }
            
        ),
        label = 'Nome', #mudando label
        # help_text = 'Texto de ajuda para o usario'  
    )
    
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept':'image/*', #qualquer imagem
            }
        )
    )

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    
    class Meta:
        model = models.Contact
        #Campos que eu quero utilizar
        fields = ('first_name','last_name','phone','email','description','category','picture') #pega do meu model

    def clean(self): #dicionario com os dados do meu formulario - garente que mesmo ocorrendo um erro, ele nao salva na db
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if first_name == last_name:
            msg = ValidationError('O Primeiro Nome não pode ser igual ao Segundo Nome',
                code='invalid')
            self.add_error('first_name',msg)
            self.add_error('last_name',msg) #campo onde eu adiciono o erro
            
        return super().clean()
