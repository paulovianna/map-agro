# -*- coding: utf-8 -*-
from django.contrib.gis.db import models


# Classes Objetos Geograficos

class Mpoly(models.Model):
    
    mpoly = models.MultiPolygonField('Multi Poligono')
    
    class Meta:
        abstract = True
        
        
class Poly(models.Model):
    
    poly = models.PolygonField('Poligono')
    
    class Meta:
        abstract = True
        
        
class Linha(models.Model):
    
    linha = models.LineStringField('Linha')
    
    class Meta:
        abstract = True
        
        
class Ponto(models.Model):
    
    ponto = models.PointField('Ponto')
    
    class Meta:
        abstract = True
        

# Classes Banco de Dados Base
  
class Pais(Mpoly):
    
    pais = models.CharField('País',max_length=64)
    sigla = models.CharField(max_length=4)
    
    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'
    
    def __unicode__(self):
        return self.pais
    
    
class Regiao(Mpoly):
    
    pais = models.ForeignKey(Pais,verbose_name='País')
    regiao = models.CharField('Região',max_length=64)
    
    class Meta:
        verbose_name = 'Região'
        verbose_name_plural = 'Regiões'
    
    def __unicode__(self):
        return self.regiao


class Uf(Mpoly):
    
    regiao = models.ForeignKey(Regiao,verbose_name='Região')
    uf = models.CharField('Unidade Federativa',max_length=64)
    
    class Meta:
        verbose_name = 'Unidades Federativa'
        verbose_name_plural = 'Unidades Federativas'
    
    def __unicode__(self):
        return self.uf
        
        
class MesoRegiao(Mpoly):
    
    uf = models.ForeignKey(Uf,verbose_name='Unidade Federativa')
    mesoRegiao = models.CharField('Mesorregião',max_length=64)
    
    class Meta:
        verbose_name = 'Mesorregião'
        verbose_name_plural = 'Mesorregiões'
    
    def __unicode__(self):
        return self.mesoRegiao
    
    
class MicroRegiao(Mpoly):
    
    mesoRegiao = models.ForeignKey(MesoRegiao,verbose_name='Mesorregião')
    microRegiao = models.CharField('Microrregião',max_length=64)
    
    class Meta:
        verbose_name = 'Microrregião'
        verbose_name_plural = 'Microrregiões'
    
    def __unicode__(self):
        return self.microRegiao
        
        
class Municipio(Mpoly):
    
    microRegiao = models.ForeignKey(MicroRegiao,verbose_name='Microrregião')
    municipio = models.CharField('Município',max_length=64)
    
    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'
    
    def __unicode__(self):
        return self.municipio
        
        
class RegiaoGeoPolitica(models.Model):
    
    municipios = models.ManyToManyField(Municipio,verbose_name='Município')
    regiaoGeoPolitica = models.CharField('Região Geopolítica',max_length=64)
    
    class Meta:
        verbose_name = 'Região Geopolítica'
        verbose_name_plural = 'Regiões GeoPolíticas'
        

# Classes Base para Pessoas    

class Pessoa(models.Model):
    
    municipio = models.ForeignKey(Municipio,verbose_name='Município')
    denominacao = models.CharField('Denominação',max_length=64)
    
    class Meta:
        abstract = True 
    
    
class PessoaFisica(Pessoa):
    
    OPCOES_SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    
    cpf = models.CharField('CPF',max_length=32)
    dataNascimento = models.DateField('Data de Nascimento')
    sexo = models.CharField('Sexo',max_length=1,choices=OPCOES_SEXO)
    
    class Meta:
        abstract = True
        
    def idade(self):  
        pass
    
    
class PessoaJuridica(Pessoa):
    
    cnpj = models.CharField('CNPJ',max_length=32)
    
    class Meta:
        abstract = True 