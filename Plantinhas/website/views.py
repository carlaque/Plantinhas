from django.shortcuts import render, redirect
from website.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    args = ''

    if request.method == "POST":
        if 'cadastrar' in request.POST:
            data = Usuario()
            data.nome = request.POST['nome']
            data.username = request.POST['username']
            data.email = request.POST['email']
            data.senha = request.POST['senha']
            data.save()
            
            return render(request, 'login.html', args)

        elif 'entrar' in request.POST:
            user = request.POST['usernameE']
            senha  = request.POST['senhaE']
            logado = Usuario.objects.filter(username = user , senha = senha).first()

            if logado is not None:
                #login com sucesso return
                return render(request, 'index.html', args)
            else:
                #alguma coisa esta errado retunr
                return render(request, 'login.html', args)



    
    return render(request, 'login.html')
