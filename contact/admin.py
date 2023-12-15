from django.contrib import admin
from contact.models import Contact,Category

# Register your models here.

#configuração do meu model na adimin do django
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone','category','show')
    ordering = ('id',) #ordenação
    search_fields = 'id','first_name','last_name', #campo de pesquisa
    list_per_page = 10 #quantidade de itens por pagina - paginação
    list_max_show_all = 100
    list_editable = 'first_name','last_name','show' #consigo editar de forma mais fácil
    list_display_links = 'id','phone' #nao pode ter no editable e no link
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display ='name',
    ordering = ('id',) #ordenação
    
    
    
