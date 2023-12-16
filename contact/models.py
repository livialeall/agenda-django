from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name #retorna a categoria (familia/amigos..)
    
#CRUD
class Contact(models.Model): #campos da tabela
    first_name = models.CharField(max_length=50,verbose_name='Nome') #quando usamos charfield precisamos usar max-length - widget de texto  - input do type texto no HTML
    last_name = models.CharField(max_length=50,blank=True,verbose_name='Sobrenome')
    phone = models.CharField(max_length=50,verbose_name='Telefone')
    email = models.EmailField(max_length=250,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True) #nao tem limitação em comparação ao ChartField
    show = models.BooleanField(default=True) #mostr automaticamente 
    picture = models.ImageField(blank=True,null=True, upload_to = 'pictures/%Y/%m') #cria uma pasta picures dentro de media com a legenda do ano e mes
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True) #on_delete -> quando eu apagar a categoria o que acontece com o contato? SET_NULL -> quando eu apagar o campo é setado para nulo nos contatos
    owner =  models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True) 
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    