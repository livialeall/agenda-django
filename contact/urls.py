from django.urls import path
from contact import views #importa o package inicializado por __init__ como se fosse o arquivo views.py

app_name = 'contact'

urlpatterns = [
    path('',views.index,name = 'index'),
    path('search/',views.search,name='search'),
    
    #contact CRUD - padrao
    path('contact/<int:contact_id>/detail/',views.contact,name='contact'),
    #criar contato -PRECISA ESTAR LOGADO
    path('contact/create/',views.create,name='create'),
    #update - parametro dinamico do contato PRECISA ESTAR LOGADO E SER DONA DO CONTATO
    path('contact/<int:contact_id>/update/',views.update,name='update'),
    #deletar contato
    path('contact/<int:contact_id>/delete/',views.delete,name='delete'),
    
    
    #USER create
    path('user/create/',views.register,name='register'),
    #USER LOGIN
    path('user/login/',views.login_view,name='login'),
    #USER LOGOUT PRECISA ESTAR LOGADO
    path('user/logout/',views.logout_view,name='logout'),
    #DADOS DE UM USUÁRIO LOGADO - PRECISA ESTAR LOGADO
    path('user/update/',views.user_update,name='user_update'),
]
