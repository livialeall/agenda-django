
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User #model para user
from . import models
from django.contrib.auth import password_validation

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
    
    #sobre escreveu meu modulo
    picture = forms.ImageField(required=False,
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

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True,error_messages={'required':'Favor digitar o seu nome'})
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ( 'first_name','last_name','email','username','password1','password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists(): #se o email que passaram no form existe na db
            self.add_error(
                'email',
                ValidationError('Ja existe um usuario com esse email',code='invalid')
            )
        return email
    
    
#alterando dados usurarios - Validação de todos os campos
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    #checa se o email tem na db
    def clean_email(self):
        email = self.cleaned_data.get('email') #email enviado no form update
        current_email = self.instance.email #email já cadastrado
        
        if current_email != email:#se o email que ela ta enviando no formulario é diferente do email cadastrado - ela quer alterar logo eu confiro se ele ja existe na db
            if User.objects.filter(email=email).exists(): #se o email que passaram no form existe na db
                self.add_error(
                    'email',
                    ValidationError('Ja existe um usuario com esse email',code='invalid')
                )
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1',ValidationError(errors))
        return password1
    
        
    def save(self,commit=True): #esta sobreescrevendo o metodo que salva na db - por isso precisa retornar o user
        cleaned_data = self.cleaned_data
        user = super().save(commit=False) #salvo os dados do usario sem puxar pra db
        
        password = cleaned_data.get('password1')
        
        if password: #salva senha do usuario de forma criptografada
            user.set_password(password)
        
        if commit:
            user.save()
        return user
    
    
     #validação de mais um campo
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não são iguais')
                )
        
        super().clean()
        
        
    class Meta:
        model = User
        fields = ( 'first_name','last_name','email','username')
        