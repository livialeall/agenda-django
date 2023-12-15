from django.shortcuts import render,get_object_or_404,redirect #ou obtem um objeto ou levanta um erro not found
from contact.models import Contact
from django.db.models import Q
from django import http
from django.core.paginator import Paginator

# Create your views here.

#Pagina que mostra os contatos
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id') #criando variavel de contato - filtrando tudo que esta com show = True
    
    
    paginator = Paginator(contacts,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj' : page_obj,
        'site_title': 'Contatos -' #extendo a base que tem essa variavel
    }
    
    return render(request,'contact/index.html',context)


#Pagina de pesquisa
def search(request):
    search_value = request.GET.get('q','').strip() #um dicionario python - selecionei pela chave = name do form - strip() - retira espços do começo e do fim
    
    if  search_value == '':
        return redirect('contact:index') #se a pessoa nao digitar nada ele redireciona para o inicio
    
    #aqui utilizamos lookups para fazer nossas pesquisas
    contacts = Contact.objects \
    .filter(show=True)\
    .filter( #Minha pesquisa de valores OU 
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value)
        
    )\
    .order_by('-id')#criando variavel de contato - filtrando tudo que esta com show = True
    
    
    paginator = Paginator(contacts,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj' : page_obj,
        'site_title': 'Contatos -'
    }
    
    return render(request,'contact/index.html',context)
    
#Pega o contato para mostrar suas informações na tela
def contact(request,contact_id): #request - requisição url q o cliente faz
    #single_contact = Contact.objects.filter(pk=contact_id).first() #busca uma unica coisa - buscaremos pelo id - unico - contact view que aparecer na url.Ele PRECISA encontrar APENAS um valor
    single_contact = get_object_or_404(Contact,pk=contact_id,show=True)
    site_title = f'{single_contact.first_name} {single_contact.last_name}'
    context = {
        'contact' : single_contact, #objeto = instancia = contato buscaso pelo id
        'site_title' : site_title
    }
    
    return render(request,'contact/contact.html',context) #renderizo a requisição, o template e o contexto = objeto


#Paginator
