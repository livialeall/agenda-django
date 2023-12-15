from django.urls import path
from contact import views #importa o package inicializado por __init__ como se fosse o arquivo views.py

app_name = 'contact'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('search/',views.search,name='search'),
    
    #contact CRUD - padrao
    path('contact/<int:contact_id>/detail/',views.contact,name='contact'),
    #criar contato
    path('contact/create/',views.create,name='create')
    
]
