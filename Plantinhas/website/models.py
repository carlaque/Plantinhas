from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome  = models.CharField(max_length=255, verbose_name='Nome')
    username = models.CharField(max_length=50, verbose_name='Username')
    senha = models.CharField(max_length=16, verbose_name='Senha')
    email = models.EmailField(verbose_name='Email')

    def __int__ (self):
        return self.codigo

class Clima(models.Model): ##mudar para clima
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name='Nome')

    def __srt__ (self):
        return self.nome

class Intencao(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255,verbose_name='Tipo')

    def __int__ (self):
        return self.codigo

class Espaco(models.Model):
    codigo = models.AutoField(primary_key=True)
    lugar = models.CharField(max_length=255, verbose_name='lugar')
    tamanho = models.CharField(max_length=255, verbose_name='tamanho')
    solo = models.CharField(max_length=255, verbose_name='solo')
    codClima = models.ForeignKey(Clima, on_delete=None) ##mudar para clima
    ##adicionar o espaço para o tipo de solo

    def __int__ (self):
        return sefl.codigo

class Planta(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name='nome', unique=True)
    diasRegar = models.IntegerField(null=True)
    luz = models.BooleanField()
    colher = models.CharField(max_length=255, verbose_name='colher')
    podar = models.CharField(max_length=255, verbose_name='podar')
    codEspaco = models.OneToOneField(Espaco, on_delete=models.CASCADE)
    venenosa = models.BooleanField()
    codTipo = models.ForeignKey(Intencao, on_delete=None)
    observacoes = models.CharField(max_length=255, verbose_name='observacoes')

    def __int__ (self):
        return self.codigo

class Jardim(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, verbose_name='nome', null=False)
    ensolarado = models.BooleanField()
    codUsuario = models.ForeignKey(Usuario, on_delete=None)

    def __int__ (self):
        return self.codigo

class Plantada(models.Model):
    codigo = models.AutoField(primary_key=True)
    codPlanta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    codJardim = models.ForeignKey(Jardim, on_delete=models.CASCADE)

    def __int__ (self):
        return self.codigo

