from django.shortcuts import render
from django.http import HttpResponse


def cadastro(request):
    return render(request, 'cadastro.html')
    #return HttpResponse('Olá from Cadastro')
    
