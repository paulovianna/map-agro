# -*- coding: utf-8 -*-
from django.contrib.gis.db import models
from geo_liberty.models import PessoaFisica,Ponto,Municipio

class Proprietario(PessoaFisica):
    
    OPCOES_ESTADO_CIVIL = (
        ('C', 'Casado'),
        ('S', 'Solteiro'),
    )
    
    telefone = models.CharField('Telefone',max_length=16)
    endereco = models.CharField('Endereço',max_length=128)
    estadoCivil = models.CharField('Estado Civil',max_length=1,choices=OPCOES_ESTADO_CIVIL)
    
    class Meta:
        abstract = True 
        
    
class Propriedade(Ponto):
    
    municipio = models.ForeignKey(Municipio,verbose_name='Município')
    #proprietario = models.ForeignKey(Proprietario,verbose_name='Proprietario')
    denominacao = models.CharField('Denominação',max_length=64)
    localizacao = models.CharField('Localização',max_length=128)
    area = models.FloatField('Área')
    
    class Meta:
        abstract = True 
    