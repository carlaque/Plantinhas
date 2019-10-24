from django.shortcuts import render, redirect
from website.models import *
from django.db.models import Q



# Create your views here.
def index(request):
    if not Clima.objects.all():
        cl = {'alta', 'amena', 'baixa', 'muito baixa'}

        for i in cl:
            x = Clima()
            x.nome = i
            x.save()

    if not Intencao.objects.all():
        inte = {'Decoração', 'Tempero' , 'Chá', 'PANC'}
        
        for i in inte:
            x = Intencao()
            x.tipo = i
            x.save()
    
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
                    'usuario' : True,
                    'dados' : logado.codigo,
                    'jardins' : Jardim.objects.filter(codUsuario = logado.codigo).first()
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
            'dados' : Usuario.objects.filter(codigo = codigo).first(),
            'listar_local' : listar_local,
            'listar_tipo'  : listar_tipo,
            'intencao' : Intencao.objects.all(),
            'temperatura' : Clima.objects.all()
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
            if codigo > 0:
                args = {
                    'usuario' : True,
                    'dados' : Usuario.objects.filter(codigo = codigo).first(),
                    'plantas' : plantas,
                    'jardins' : Jardim.objects.filter(codUsuario = Usuario.objects.filter(codigo = codigo).first()).all()
                }
            else:
                args = {
                    'usuario' : False,
                    'dados' : Usuario.objects.filter(codigo = codigo).first(),
                    'plantas' : plantas,
                    'jardins' : Jardim.objects.filter(codUsuario = Usuario.objects.filter(codigo = codigo).first()).all()
                }

            return render(request, 'plantas.html', args)
    
    if codigo > 0:
        if request.method == 'POST':
            plantada = Plantada()
            plant = Planta.objects.filter(codigo=request.POST['codigo']).first()
            jard =Jardim.objects.filter(codUsuario=codigo,codigo=request.POST['jardim']).first()
            plantada.codJardim = jard
            plantada.codPlanta = plant
            plantada.save()

            args = {
                'usuario' : True,
                'dados' : Usuario.objects.filter(codigo = codigo).first(),
                'plantas' : Planta.objects.all(),
                'jardins' : Jardim.objects.filter(codUsuario = Usuario.objects.filter(codigo = codigo).first()).all()
            }
            return render(request, 'plantas.html', args)

    if codigo == 0:
        args = {
            'plantas' : Planta.objects.all(),
            'usuario' : False
        }
    else: 
        args = {
            'plantas' : Planta.objects.all(),
            'dados' : Usuario.objects.filter(codigo = codigo).first(),
            'jardins' : Jardim.objects.filter(codUsuario = Usuario.objects.filter(codigo = codigo).first()).all(),
            'usuario' : True
        }     
    
    return render(request, 'plantas.html', args )

def usuario(request, codigo):
    dados = {}
    if codigo > 0 :
        dados = Usuario.objects.filter(codigo = codigo).first()
    
        if request.method == 'POST':
            if 'plantada' in request.POST :
                jardim = Jardim.objects.filter(codigo = request.POST['plantada'] ).first()
                args = {
                    'dados' : dados
                }
                return redirect('/jardim/plantas/' + str(dados.codigo) + '/'+ str(jardim.codigo), args)
            else:
                args = {
                    'dados' : dados
                }
                return redirect('/jardim/cadastro/' + str(dados.codigo), args)

        args = {
            'usuario' : True,
            'jardins' : Jardim.objects.filter(codUsuario = codigo).all(),
            'dados' : dados
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
                j.ensolarado = False
                args = {
                    'luz' : False ,
                    'espaco' : request.POST['lugar'] ,
                    'intencao' : request.POST['intencao'],
                    'temperatura' : request.POST['temperatura'] 
                }

            j.codUsuario = Usuario.objects.filter(codigo = codigo).first()
            j.save()

            return redirect('/plantas/' + str(dados.codigo) + '?nome=&espaco='+ request.POST['lugar'] + '&intencao=' +  request.POST['intencao'] +  '&temperatura=' +  request.POST['temperatura'] + '&mostrar=')
    
    args = {
        'intencao' : Intencao.objects.all(),
        'temperatura' : Clima.objects.all()
    }

    return render(request, 'jardim-cadastro.html', args)

def plantadas(request, codigo, jardim):
    dados = {}
    if codigo > 0:
        dados = Usuario.objects.filter(codigo = codigo).first()

        if request.method == 'POST':
            if 'deletar' in request.POST:
                p = Plantada()
                p = Plantada.objects.filter(codPlanta = request.POST['deletar'], codJardim = jardim ).first()
                p.delete()

                args = {
                    'dados' : Usuario.objects.filter(codigo = codigo).first(),
                    'msg' : 'A planta ' + str(Planta.objects.filter(codigo = request.POST['deletar']).first()) + ' foi retirada desse jardim',
                    'jardim' : Jardim.objects.filter(codigo = jardim).first(),
                    'plantadas' : Plantada.objects.filter(codJardim = jardim).all()
                }

                return render(request, 'jardim-plantas.html', args)
            else:
                return redirect('/plantas/' + str(codigo))

        
        args = {
            'dados' : Usuario.objects.filter(codigo = codigo).first(),
            'jardim' : Jardim.objects.filter(codigo = jardim).first(),
            'plantadas' : Plantada.objects.filter(codJardim = jardim).all()
        }
        return render(request, 'jardim-plantas.html', args)