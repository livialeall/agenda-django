from django.db import models
from django.utils import timezone

# Create your models here.

#CRUD
class Contact(models.Model): #campos da tabela
    first_name = models.CharField(max_length=50) #quando usamos charfield precisamos usar max-length
    last_name = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True) #nao tem limitação em comparação ao ChartField
    show = models.BooleanField(default=True) #mostr automaticamente 
    picture = models.ImageField(blank=True, upload_to = 'pictures/%Y/%m') #cria uma pasta picures dentro de media com a legenda do ano e mes
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    