
from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render,get_object_or_404,redirect #ou obtem um objeto ou levanta um erro not found
from contact.models import Contact
from django.db.models import Q
from django import http
from django.core.paginator import Paginator


# Create your views here.
#formulario
class ContactForm(forms.ModelForm): #baseado no model que eu ja tenho
    class Meta:
        model = Contact
        #Campos que eu quero utilizar
        fields = ('first_name','last_name','phone',)
        
    def clean(self): #dicionario com os dados do meu formulario
        cleaned_data = self.cleaned_data
        
        #simulando erro - validação de campo
        self.add_error(
            'first_name', #onde eu quero adicionar o erro
            ValidationError( #classe de erro de validação
                'Mensagem de Erro',code='invalid' 
            )
            
        )
        return super().clean()
def create(request):
    
    if request.method == 'POST':
        
        context = {
        'form': ContactForm(request.POST) #cria uma instancia - dados do formulario postado
        
    }
        return render(request,'contact/create.html',context)

    #caso seja get
    context = {
        'form': ContactForm() #cria uma instancia
    }
    
    return render(request,'contact/create.html',context)
