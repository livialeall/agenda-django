from django.contrib import admin
from contact.models import Contact

# Register your models here.

#configuração do meu model na adimin do django
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone',)
    ordering = ('id',) #ordenação
    search_fields = 'id','first_name','last_name', #campo de pesquisa
    list_per_page = 10 #quantidade de itens por pagina - paginação
    list_max_show_all = 100
    list_editable = 'first_name','last_name', #consigo editar de forma mais fácil
    list_display_links = 'id','phone' #nao pode ter no editable e no link