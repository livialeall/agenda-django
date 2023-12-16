from django.shortcuts import render,redirect
from django.contrib import messages
from contact.forms import RegisterForm,RegisterUpdateForm #classe que cria formulario de registro
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def register(request):
    form = RegisterForm()
    # messages.info(request,'INFORMACAO') #enviei a mensagem

    # messages.warning(request,'INFORMACAO') #enviei a mensagem
    # messages.error(request,'INFORMACAO') #enviei a mensagem
    
    if request.method == 'POST': #se for um formualrio do tipo post e nao apenas uma renderização tipo GET eu salvo na db
        form = RegisterForm(request.POST) #envio os dados do POST para o form
        
        if form.is_valid(): #se for valido eu salvo na base de dados
            form.save()
            messages.success(request,'Usuario registrado com sucesso') #enviei a mensagem na pagina redirecionada
            return redirect('contact:index')
            
    return render(request,'contact/register.html',{
        'form' : form
    })
    
    
def login_view(request):
    form = AuthenticationForm(request)
    
    if request.method =='POST': 
        form = AuthenticationForm(request,data=request.POST)
        
        if form.is_valid():
            user = form.get_user() #pego o usario que foi passado na requisição
            auth.login(request,user)
            messages.success(request,'Login feito com sucesso')
        else:
            messages.error(request,'Login Invalido')
    
    return render(request,'contact/login.html',{
        'form' : form
    })
    
@login_required(login_url='contact:login') #caso nao esteja logado ele redireciona     
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')
    

@login_required(login_url='contact:login') #caso nao esteja logado ele redireciona  
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)#forçar o usuario a estar logado
    
    if request.method != 'POST': #se o metodo não for post - eu renderizo
        return render(
            request,'contact/user_update.html',{
            'form' : form
        })
        
    form = RegisterUpdateForm(data=request.POST,instance=request.user) #se for POST eu passo os dados do formulario 
    
    if not form.is_valid(): #se nao fro valido eu me mantenho no formulario
        return render(
            request,'contact/user_update.html',{
            'form' : form
        })
        
    form.save() #se for valido eu salvo na db
    return redirect('contact:user_update') #atualiza a pagina sem reenviar o usuario