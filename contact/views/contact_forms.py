from django.shortcuts import render,get_object_or_404,redirect #ou obtem um objeto ou levanta um erro not found
from contact.models import Contact
from django import http
from django.urls import reverse #consigo passar dados dentro da função para ela retornar uma url do seu contato
from contact.forms import ContactForm


# Create your views here.

#Cria um contato
def create(request):
    form_action = reverse('contact:create')
    
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES)
        
        context = {
        'form': form, #cria uma instancia - dados do formulario postado
        'form_action':form_action,
        }
        
        if form.is_valid(): #verifico se é valido para enviar os dados par algum lugar
            contact = form.save() #salva na db - Podemos usar commit = False ele nao envia pra db, mas salva na memoria
            return redirect('contact:update',contact_id=contact.pk) #redirecionar para url de edição
  
        return render(request,'contact/create.html',context)

    #caso seja get
    context = {
        'form': ContactForm(), #cria uma instancia
        'form_action':form_action,
    }
    
    return render(request,'contact/create.html',context) #aqui passo caminho do template


#Redirecionada quando cria para atualizar o contato
def update(request,contact_id):
    contact = get_object_or_404(
        Contact,pk=contact_id,show=True)
    form_action = reverse('contact:update',args=(contact_id,)) #parametro dinamico da url
    
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES,instance=contact) #utilizo a instance para passar as informações do contact - criado pelo objeto - request.FILES -> arquivos da requisição enviada
        
        context = {
        'form': form, #cria uma instancia - dados do formulario postado
        'form_action':form_action,
        }
        
        if form.is_valid(): #verifico se é valido para enviar os dados par algum lugar
            contact = form.save() #salva na db - Podemos usar commit = False ele nao envia pra db, mas salva na memoria
            return redirect('contact:update',contact_id=contact.pk) #redirecionar para url de edição
  
        return render(request,'contact/create.html',context)

    #caso seja get
    context = {
        'form': ContactForm(instance=contact), #cria uma instancia
        'form_action':form_action,
    }
    
    return render(request,'contact/create.html',context) #aqui passo caminho do template


#deletar

def delete(request,contact_id):
    contact = get_object_or_404(
        Contact,pk=contact_id,show=True)
    
    confirmation = request.POST.get('confirmation','no')
    
    if confirmation == 'yes': #botao de yes do input com o nome confirmation
        contact.delete()
        return redirect('contact:index')
    
    
    return render(request,'contact/contact.html',{
        'contact':contact,
        'confirmation':confirmation
    })