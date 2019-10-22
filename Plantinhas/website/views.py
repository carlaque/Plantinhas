from django.shortcuts import render, redirect
from website.models import *
from django.db.models import Q



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
            logado = Usuario.objects.filter(username = user, senha = senha).first()

            if logado is not None:
                args = {
                    'dados' : logado.codigo
                }
                aux = '/usuario/' + str(logado.codigo)
                return redirect(aux, args)
            else:
                args = {
                    'msgErro': 'Ops! Algo de errado não esta certo... por favor tente novamente'
                }
                return render(request, 'login.html', args)

    
    return render(request, 'login.html')

def plantasCad(request, codigo):    

    if request.method == 'POST':
        e = Espaco()
        e.lugar = request.POST['lugar']
        e.tamanho = request.POST['tamanho']
        e.codClima = Clima.objects.filter(codigo=request.POST['Local']).first()
        e.solo = request.POST['solo']
        e.save()

        p = Planta()
        p.nome = request.POST['nome']
        p.diasRegar = request.POST['diasRegar']
        
        if 'luz' in request.POST:
            p.luz = True
        else: 
            p.luz = False
        
        if 'venenosa' in request.POST:
            p.venenosa = True
        else: 
            p.venenosa = False
        
        p.colher = request.POST['colher']
        p.podar = request.POST['podar']
        p.codTipo = Intencao.objects.filter(codigo = request.POST['tipo']).first()
        p.codEspaco = Espaco.objects.filter(codClima = request.POST['Local'], tamanho = request.POST['tamanho'], lugar = request.POST['lugar']).last()
        p.observacoes = request.POST['obs']
        p.save()


    
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

def plantas(request, codigo):

    if request.method == 'GET':

        if 'mostrar' in request.GET:
            nome = request.GET.get('nome')
            espaco = request.GET.get('espaco')
            intencao = request.GET.get('intencao')
            temp = request.GET.get('temperatura')

            plantas = {}
            for p in Espaco.objects.filter(lugar = espaco, codClima = temp).all():
                if nome != '' :
                    plantas = Planta.objects.filter(Q(nome=nome) & Q(codEspaco = Espaco.objects.filter(codigo = p, lugar = espaco).first()) | Q(codTipo=intencao)).distinct()
                else:
                    plantas = Planta.objects.filter(Q(nome=nome) | Q(codEspaco = Espaco.objects.filter(codigo = p, lugar = espaco).first()) | Q(codTipo=intencao)).distinct()
            
            args = {
                'plantas' : plantas
            }
            return render(request, 'plantas.html', args)



    args = {
        'plantas' : Planta.objects.all()
    }
    return render(request, 'plantas.html', args)


def usuario(request, codigo):
    dados = {}
    if codigo > 0 :
        dados = Usuario.objects.filter(codigo = codigo).first()
    

    if request.method == 'POST':
        args = {
            'dados' : dados
        }
        return redirect('/jardim/cadastro/' + str(dados.codigo), args)

    jardins = Jardim.objects.filter(codUsuario = 1).first()

    args = {
        'dados' : dados,
        'jardins' : jardins
    }
    return render(request, 'usuario.html', args)
    


def jardimCad(request, codigo):
    dados = {}
    if codigo > 0 :
        dados = Usuario.objects.filter(codigo = codigo).first()
    

    if request.method == 'POST':
        args = {}
        j = Jardim()
        j.nome = request.POST['nome']
        if 'ensolarado' in request.POST:
            j.ensolarado = True
            args = {
                'luz' : True ,
                'espaco' : request.POST['lugar'] ,
                'intencao' : request.POST['intencao'],
                'temperatura' : request.POST['temperatura'] 
            }
        else:
            args = {
                'luz' : False ,
                'espaco' : request.POST['lugar'] ,
                'intencao' : request.POST['intencao'],
                'temperatura' : request.POST['temperatura'] 
            }

        j.codUsuario = Usuario.objects.filter(codigo = codigo).first()
        j.save()

        return redirect('/plantas/' + str(dados.codigo) + '?nome=&espaco='+ request.POST['lugar'] + '&intencao=' +  request.POST['intencao'] +  '&temperatura=' +  request.POST['temperatura'])


    return render(request, 'jardim-cadastro.html')
