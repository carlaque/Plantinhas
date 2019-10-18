from django.shortcuts import render, redirect
from website.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):

    if request.method == "POST":
        if 'cadastrar' in request.POST:
            data = Usuario()
            data.nome = request.POST['nomeC']
            data.username = request.POST['usernameC']
            data.email = request.POST['emailC']
            data.senha = request.POST['senhaC']
            data.save()
            args={
                'msgCad': 'Cadastrado com sucesso! Faça o login ao lado.'
            }
            return render(request, 'login.html', args)

        elif 'entrar' in request.POST:
            user = request.POST['usernameE']
            senha  = request.POST['senhaE']
            logado = Usuario.objects.filter(username = user, senha = senha). first()

            if logado is not None:
                #FAZER O REDIRECT PARA A PAGINA DO USUARIO
                return render(request, 'index.html')
            else:
                args = {
                    'msgErro': 'Ops! Algo de errado não esta certo... por favor tente novamente'
                }
                return render(request, 'login.html', args)

    
    return render(request, 'login.html')

def plantasCad(request):

    if request.method == 'POST':
        e = Espaco()
        e.lugar = request.POST['lugar']
        e.tamanho = request.POST['tamanho']
        e.codClima = request.POST['Local']
        e.solo = request.POST['solo']
        e.save()

        p = Planta()
        p.nome = request.POST['nome']
        p.diasRegar = request.POST['diasRegar']
        p.luz = request.POST['luz']
        p.colher = request.POST['colher']
        p.podar = request.POST['podar']
        p.codTipo = request.POST['tipo']
        p.codEspaco = Espaco.objects.last().codigo       
        p.observacoes = request.POST['obs']
        p.save()
        
        args = {
            'msg': 'cad sucesso gay'
        }

        return render(request, 'plantas-cadastro.html', args)

    
    listar_local = Clima.objects.all()
    listar_tipo = Intencao.objects.all()

    args = None
    if listar_local.first() is None and listar_tipo.first() is None:
        args = {
            'msg' : 'Nada cadastrado ainda'
        }
    else:
        args = {
            'listar_local' : listar_local,
            'listar_tipo'  : listar_tipo
        }

    return render(request, 'plantas-cadastro.html', args)


