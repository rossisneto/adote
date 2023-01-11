from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method =='GET':
        return render(request, 'cadastro.html')
    #return HttpResponse('Olá from Cadastro')
    elif request.method == 'POST':
        nome=request.POST['nome']
        email=request.POST['email']
        senha=request.POST['senha']
        confirmar_senha=request.POST['confirmar_senha']


        if len(nome.strip())==0 or len(email.strip())==0 or len(senha.strip())==0 or len(confirmar_senha.strip())==0:
            #return HttpResponse('Há campos que não foram preenchidos !!!')    #return nome + ' ' + email
            messages.add_message(request, constants.ERROR,'Preencha todos os campos')
            print('erro de campos vazios')
            return render(request,'cadastro.html')
        if senha!= confirmar_senha:
            messages.add_message(request, constants.ERROR,'Senhas informadas não conferem')
            print('erro de confirmação de senha')
            return render(request,'cadastro.html')
        try:
            user=User.objects.create_user(username=nome, email=email,password=senha)
            #mensagem de sucesso:
            messages.add_message(request, constants.SUCCESS,'Usuario incluido')
            return HttpResponse(f'<h1>Usuario incluido<h1>!!!<br>{nome}<br>{email}<br>{senha}<br>{confirmar_senha}')
        except:
            messages.add_message(request, constants.ERROR,'Falha na inclusão do usuário')
            return HttpResponse(f'<h1>Falha na inclusao do usuario<h1>!!!<br>{nome}<br>{email}<br>{senha}<br>{confirmar_senha}')

        else:
            return HttpResponse(f'Não são permitidas requisições do tipo {request.method}')
    
def logar(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    
    if request.method == 'GET':
        #return HttpResponse('Pagina de login')
        return render(request,'login.html')
    elif request.method == 'POST':
        nome=request.POST.get('nome')
        senha=request.POST.get('senha')
        user=authenticate(username=nome,password=senha)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/divulgar/novo_pet')
            #return HttpResponse(f'{nome} {senha}')

        else:
            messages.add_message(request, constants.ERROR,'Usuario ou senha incorretos')
            print('Usuario não encontrado ou a senha está incorreta')
            return render(request,'login.html')
    else:
        return HttpResponse('Falha')


def sair(request):
    logout(request)
    return(redirect, '/auth/login')