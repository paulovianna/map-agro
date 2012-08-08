# -*- coding: utf-8 -*-
from django.contrib.gis.db import models
from geo_liberty.smart_selects.db_fields import ChainedForeignKey 
from geo_liberty.models import PessoaFisica,Ponto,Municipio

#Classes Abstratas

class Proprietario(PessoaFisica):
    
    OPCOES_ESTADO_CIVIL = (
        ('Casado', 'Casado(a)'),
        ('Solteiro', 'Solteiro(a)'),
        ('Separado', 'Separado(a)'),
        ('Viuvo', 'Viúvo(a)'),
    )
    
    municipio = models.ForeignKey(Municipio,default=4321329)
    rg = models.CharField('RG',max_length=16)
    telefone = models.CharField('Telefone',max_length=16,blank=True)
    endereco = models.CharField('Endereço',max_length=32)
    estadoCivil = models.CharField('Estado Civil',max_length=16,choices=OPCOES_ESTADO_CIVIL)
    
    class Meta:
        abstract = True 
        
    
class Propriedade(Ponto):
    
    #uf = models.ForeignKey(Uf,verbose_name='Unidade Federativa')
    #mesoRegiao = ChainedForeignKey(MesoRegiao, chained_field="uf",chained_model_field="uf",verbose_name='Mesorregião')
    #microRegiao = ChainedForeignKey(MicroRegiao, chained_field="mesoRegiao",chained_model_field="mesoRegiao",verbose_name='Microrregião')
    #municipio = ChainedForeignKey(Municipio, chained_field="microRegiao",chained_model_field="microRegiao",verbose_name='Município')
    municipio = models.ForeignKey(Municipio,default=4321329)
    denominacao = models.CharField('Denominação',max_length=32)
    localizacao = models.CharField('Localização',max_length=32)
    area = models.FloatField('Área')
    
    class Meta:
        abstract = True 
    
    def __unicode__(self):
        return self.denominacao
      
          
#Beneficiário

class Classificacao(models.Model):
    
    situacao = models.CharField('Situação',max_length=32)
   
    class Meta:
        verbose_name = 'Classificação'
        verbose_name_plural = 'Classificações'
        
    def __unicode__(self):
        return self.situacao

      
class Beneficiario(Proprietario):
    
    SITUACAO = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    )
    
    dap = models.CharField('Nº DAP',max_length=20)
    situacao = models.CharField('Situação',max_length=16,choices=SITUACAO)
    classificacao = models.ForeignKey(Classificacao,verbose_name='Classificação')

    class Meta:
        verbose_name = 'Beneficiário'
        verbose_name_plural = 'Beneficiários'
        ordering = ['denominacao']
      

class Familia(PessoaFisica):
    
    parentesco = models.CharField('Parentesco',max_length=16)
    dap = models.CharField('Nº DAP',max_length=16,blank=True)
    beneficiario = models.ForeignKey(Beneficiario,verbose_name='Beneficiario')

    class Meta:
        verbose_name = 'Membro da Família'
        verbose_name_plural = 'Membros da Família'
    
    def idade(self):
        from datetime import date
        return ((date.today() - self.dataNascimento).days) / 365
    

#Informações Gerais Unidade de Produção

class DestinoLixo(models.Model):
    
    TIPO_LIXO = (
        ('Organico', 'Orgânico'),
        ('Inorganico', 'Inorgânico'),
    )
    
    destino = models.CharField('Destino do Lixo',max_length=32)
    tipoLixo = models.CharField('Tipo Lixo',max_length=16,choices=TIPO_LIXO)
     
    class Meta:
        verbose_name = 'Destino do Lixo'
        verbose_name_plural = 'Destinos do Lixo'
        
    def __unicode__(self):
        return self.destino
        

class Agrotoxico(models.Model):
    
    agrotoxico = models.CharField('Agrotóxico',max_length=32)
    
    class Meta:
        verbose_name = 'Agrotóxico'
        verbose_name_plural = 'Agrotóxicos'
        
    def __unicode__(self):
        return self.agrotoxico
        
        
class DestinoEmbalagemAgrotoxico(models.Model):
    
    destino = models.CharField('Destino de Embalagem de Agrotóxico',max_length=32)
    
    class Meta:
        verbose_name = 'Destino de Embalagem de Agrotóxico'
        verbose_name_plural = 'Destinos de Embalagem de Agrotóxico'
        
    def __unicode__(self):
        return self.destino
    
 
class PreparoSolo(models.Model):
    
    preparoSolo = models.CharField('Preparo do Solo',max_length=16)
    
    class Meta:
        verbose_name = 'Preparo do Solo'
        verbose_name_plural = 'Preparos do Solo'
     
    def __unicode__(self):
        return self.preparoSolo
    
       
class InsumosOrganicos(models.Model):
    
    insumoOrganico = models.CharField('Insumo Orgânico',max_length=32)
    
    class Meta:
        verbose_name = 'Insumo Orgânico'
        verbose_name_plural = 'Insumos Orgânicos'
        
    def __unicode__(self):
        return self.insumoOrganico


class UtilizacaoArvores(models.Model):
    
    utilizacaoArvore = models.CharField('Utilização de Árvores',max_length=32)
    
    class Meta:
        verbose_name = 'Utilização de Árvore'
        verbose_name_plural = 'Utilizações de Árvore'
        
    def __unicode__(self):
        return self.utilizacaoArvore
    
        
class PraticaConservacaoSolo(models.Model):
    
    conservacaoSolo = models.CharField('Prática de Conservação do Solo',max_length=32)
    
    class Meta:
        verbose_name = 'Prática de Conservação do Solo'
        verbose_name_plural = 'Práticas de Conservação do Solo'
        
    def __unicode__(self):
        return self.conservacaoSolo
        

#Unidade de Produção

class UnidadeProducao(Propriedade):
    
    QUALIDADE_AGUA = (
        ('Boa', 'Boa'),
        ('Regular', 'Regular'),
        ('Ruim', 'Ruim'),
    )
    
    beneficiario = ChainedForeignKey(Beneficiario, chained_field="municipio",chained_model_field="municipio",verbose_name=u'Beneficiário')
    participacao = models.DecimalField(u'Participação %',max_digits=8,decimal_places=2,blank=True,null=True)
    tituloDominio = models.CharField(u'Título de Domínio',max_length=16,blank=True)
    dataRegistro = models.DateField(u'Data de Registro',blank=True,null=True)
    registro = models.CharField(u'Registro',max_length=16,blank=True)
    receitaFederal = models.CharField(u'Nº Receita Federal (ITR)',max_length=16)
    qualidadeAgua = models.CharField(u'Qualidade da Água',max_length=8,choices=QUALIDADE_AGUA,blank=True)
    destinoLixo = models.ManyToManyField(DestinoLixo,verbose_name=u'Destino do Lixo',blank=True)
    utilizacaoAgrotoxico = models.ManyToManyField(Agrotoxico,verbose_name=u'Utilização de Agrotóxicos',blank=True)
    destinoEmbalagemAgrotoxico = models.ManyToManyField(DestinoEmbalagemAgrotoxico,verbose_name=u'Destino da Embalagem de Agrotóxico',blank=True)
    preparoSolo = models.ManyToManyField(PreparoSolo,verbose_name=u'Preparo do Solo',blank=True)
    areaErosao = models.DecimalField(u'Área com Erosão',max_digits=8,decimal_places=2,blank=True,null=True,default='0.0')
    praticaConservacaoSolo = models.ManyToManyField(PraticaConservacaoSolo,verbose_name=u'Pratica de Conservação do Solo',blank=True)
    insumosOrganicos = models.ManyToManyField(InsumosOrganicos,verbose_name=u'Insumos Orgânicos',blank=True)
    rotacaoCultura = models.BooleanField(u'Rotação de Cultura',blank=True)
    utilizacaoArvores = models.ManyToManyField(UtilizacaoArvores,verbose_name=u'Utilização de Árvores',blank=True)
    
    class Meta:
        verbose_name = u'Unidade de Produção Familiar'
        verbose_name_plural = u'Unidades de Produção Familiar'
        ordering = ['beneficiario__denominacao']
        
    def get_absolute_url(self):
        return '/mapagro/unidade/%i/' % self.id
    
    def get_beneficiario_url(self):
        return '/mapagro/beneficiario/%i/' % self.beneficiario.id
    
    def get_renda_url(self):
        return '/mapagro/renda/%i/%i/' % (self.id, self.beneficiario.id)
    
    

class Confrontacao(models.Model):
    
    unidadeProducao = models.ForeignKey(UnidadeProducao,verbose_name='Unidade de Produção Familiar')
    norte = models.CharField('Norte',max_length=32)
    sul = models.CharField('Sul',max_length=32)
    leste = models.CharField('Leste',max_length=32)
    oeste = models.CharField('Oeste',max_length=32)
    roteiroAcesso = models.TextField('Roteiro de Acesso',blank=True)
    
    class Meta:
        verbose_name = 'Confrontação'
        verbose_name_plural = 'Confrontações'
    
    
class Terra(models.Model):
    
    usoAtual = models.CharField('Uso Atual',max_length=16)
    terras = models.ManyToManyField(UnidadeProducao, through='Terra_UnidadeProducao')
    
    class Meta:
        verbose_name = 'Terra'
        verbose_name_plural = 'Terras'
        
    def __unicode__(self):
        return self.usoAtual
        
        
class Terra_UnidadeProducao(models.Model):
    
    unidadeProducao = models.ForeignKey(UnidadeProducao,verbose_name='Unidade de Produção')
    terra = models.ForeignKey(Terra)
    area = models.DecimalField('Área',max_digits=16,decimal_places=2)
    valorUnitario = models.DecimalField('Valor Unitário',max_digits=8,decimal_places=2)
    
    class Meta:
        verbose_name = 'Terra de Unidade de Produção'
        verbose_name_plural = 'Terras de Unidade de Produção'
        
    def valorTotal(self):
        return self.area * self.valorUnitario
        

class Benfeitoria(models.Model):
    
    UNIDADE = (
        ('M3', 'M³'),
        ('M2', 'M²'),
        ('Km', 'Km'),
        ('Un', 'Un'),
    )
    
    benfeitoria = models.CharField('Benfeitoria',max_length=32)
    unidadeMedida = models.CharField('Unidade de Medida',max_length=2,choices=UNIDADE)
    benfeitorias= models.ManyToManyField(UnidadeProducao, through='Benfeitoria_UnidadeProducao')
    
    class Meta:
        verbose_name = 'Benfeitoria'
        verbose_name_plural = 'Benfeitorias'
        
    def __unicode__(self):
        return self.benfeitoria


class Benfeitoria_UnidadeProducao(models.Model):
    
    unidadeProducao = models.ForeignKey(UnidadeProducao)
    benfeitoria = models.ForeignKey(Benfeitoria,verbose_name='Benfeitoria')
    quantidade = models.DecimalField('Quantidade',max_digits=3,decimal_places=2)
    valorUnitario = models.DecimalField('Valor Unitário',max_digits=8,decimal_places=2)
    obervacoes = models.TextField('Observações',blank=True)
    
    class Meta:
        verbose_name = 'Benfeitoria de Unidade de Produção'
        verbose_name_plural = 'Benfeitorias de Unidade de Produção'
        
    def valorTotal(self):
        return self.quantidade * self.valorUnitario


class EquipamentoTrabalho(models.Model):
    
    equipamentoTrabalho = models.CharField('Equipamento de Trabalho',max_length=32)
    equipamentosTrabalho= models.ManyToManyField(UnidadeProducao, through='EquipamentoTrabalho_UnidadeProducao')
    
    class Meta:
        verbose_name = 'Equipamento de Trabalho'
        verbose_name_plural = 'Equipamentos de Trabalho'
        
    def __unicode__(self):
        return self.equipamentoTrabalho


class EquipamentoTrabalho_UnidadeProducao(models.Model):
    
    unidadeProducao = models.ForeignKey(UnidadeProducao)
    equipamentoTrabalho = models.ForeignKey(EquipamentoTrabalho,verbose_name='Equipamento de Trabalho')
    quantidade = models.IntegerField('Quantidade')
    valorUnitario = models.DecimalField('Valor Unitário',max_digits=8,decimal_places=2)
    capacidadePotencia = models.CharField('Capacidade(Kg) / Potência(Cv)',max_length=8)
    mediaIdade = models.IntegerField('Média de Idade(anos)')
    
    class Meta:
        verbose_name = 'Equipamento de Trabalho de Unidade de Produção'
        verbose_name_plural = 'Equipamentos de Trabalho de Unidade de Produção'
        
    def valorTotal(self):
        return self.quantidade * self.valorUnitario


#Classes Abstratas para Agropecuária,Bovinos,Suinos,Caprinos,Aves

class AnimalTerrestre(models.Model):
    
    SISTEMA_PRODUCAO = (
        ('Intensivo', 'Intensivo'),
        ('Semi-intensivo', 'Semi-intensivo'),
        ('Extensivo', 'Extensivo'),
    )
    
    unidadeProducao = models.ForeignKey(UnidadeProducao,verbose_name='Unidade de Produção')
    sistemaProducao = models.CharField('Sistema de Produção',max_length=16,choices=SISTEMA_PRODUCAO)
    quantidade = models.IntegerField('Quantidade')
    mediaIdade = models.IntegerField('Idade Média(mês)')
    raca = models.CharField('Raça',max_length=16)
    valorUnitario = models.DecimalField('Valor Unitário',max_digits=8,decimal_places=2)
    localizacao = models.CharField('Localização',max_length=32,blank=True)
    
    class Meta:
        abstract = True
        
    def valorTotal(self):
        return self.quantidade * self.valorUnitario
        

class TipoProdutoAnimal(models.Model):
    
    UNIDADE = (
        ('Litro', 'Litro'),
        ('Kg/vivo', 'Kg/vivo'),
        ('Dúzia', 'Dúzia'),
        ('Un', 'Un'),
        ('Kg', 'Kg'),
    )
    
    produto = models.CharField('Produto',max_length=16)
    unidadeMedida = models.CharField('Unidade de Medida',max_length=16,choices=UNIDADE)
    
    class Meta:
        abstract = True
        
    def __unicode__(self):
        return self.produto
    
class ProdutoUnidadeProducao(models.Model):
    
    #uf = models.ForeignKey(Uf,verbose_name='Unidade Federativa')
    #mesoRegiao = ChainedForeignKey(MesoRegiao, chained_field="uf",chained_model_field="uf",verbose_name='Mesorregião')
    #microRegiao = ChainedForeignKey(MicroRegiao, chained_field="mesoRegiao",chained_model_field="mesoRegiao",verbose_name='Microrregião')
    #municipio = ChainedForeignKey(Municipio, chained_field="microRegiao",chained_model_field="microRegiao",verbose_name='Município')
    municipio = models.ForeignKey(Municipio,default=4321329)
    beneficiario = ChainedForeignKey(Beneficiario, chained_field="municipio",chained_model_field="municipio",verbose_name='Beneficiário')
    unidadeProducao = ChainedForeignKey(UnidadeProducao, chained_field="beneficiario",chained_model_field="beneficiario",verbose_name='Unidade de Produção')
    
    class Meta:
        abstract = True
        
    def __unicode__(self):
        return self.beneficiario.denominacao + ' - ' + self.unidadeProducao.denominacao
         

class Produto(models.Model):
    
    valorUnitario = models.DecimalField('Valor Unitário',max_digits=8,decimal_places=2)


class ProdutoAnimal(Produto):
    
    quantidade = models.IntegerField('Quantidade')
            
    class Meta:
        abstract = True
        
    def valorTotal(self):
        return self.quantidade * self.valorUnitario
         
        
#Bovinos

class TipoBovino(models.Model):
    
    tipo = models.CharField('Tipo de Bovino',max_length=16)
    
    class Meta:
        verbose_name = 'Tipo de Bovino'
        verbose_name_plural = 'Tipos de Bovinos'
    
    def __unicode__(self):
        return self.tipo
        
        
class Bovino(AnimalTerrestre):
    
    tipoBovino = models.ForeignKey(TipoBovino,verbose_name='Tipo de Bovino')
    
    class Meta:
        verbose_name = 'Bovino'
        verbose_name_plural = 'Bovinos'
        
        
class TipoProdutoBovinocultura(TipoProdutoAnimal):
    
    class Meta:
        verbose_name = 'Tipo Produto Bovinocultura'
        verbose_name_plural = 'Tipos Produto Bovinocultura'
        
        
class Bovinocultura(ProdutoUnidadeProducao):
    
    class Meta:
        verbose_name = 'Bovinocultura'
        verbose_name_plural = 'Bovinocultura'
        

class ProdutoBovinocultura(ProdutoAnimal):
    
    bovinocultura = models.ForeignKey(Bovinocultura,verbose_name='Bovinocultura')
    tipoProdutoBovino = models.ForeignKey(TipoProdutoBovinocultura,verbose_name='Tipo Produto')     

    class Meta:
        verbose_name = 'Produto Bovinocultura'
        verbose_name_plural = 'Produtos Bovinocultura'
        
        
#Suínos
    
class TipoSuino(models.Model):
    
    tipo = models.CharField('Tipo de Suíno',max_length=16)
    
    class Meta:
        verbose_name = 'Tipo de Suíno'
        verbose_name_plural = 'Tipos de Suínos'
        
    def __unicode__(self):
        return self.tipo
        
        
class Suino(AnimalTerrestre):
    
    tiposuino = models.ForeignKey(TipoSuino,verbose_name='Tipo de Suíno')
    
    class Meta:
        verbose_name = 'Suíno'
        verbose_name_plural = 'Suínos'  
        

class TipoProdutoSuinocultura(TipoProdutoAnimal):
    
    class Meta:
        verbose_name = 'Tipo Produto Suinocultura'
        verbose_name_plural = 'Tipos Produto Suinocultura'
        

class Suinocultura(ProdutoUnidadeProducao):
    
    class Meta:
        verbose_name = 'Suinocultura'
        verbose_name_plural = 'Suinocultura'
        

class ProdutoSuinocultura(ProdutoAnimal):
    
    suinocultura = models.ForeignKey(Suinocultura,verbose_name='Suinocultura')
    tipoProdutoSuino = models.ForeignKey(TipoProdutoSuinocultura,verbose_name='Tipo Produto')     

    class Meta:
        verbose_name = 'Produto Suinocultura'
        verbose_name_plural = 'Produtos Suinocultura'
        
        
#Ovinos e Caprinos

class TipoOvinoCaprino(models.Model):
    
    tipo = models.CharField('Tipo de Ovino/Caprino',max_length=16)
    
    class Meta:
        verbose_name = 'Tipo de Ovino/Caprino'
        verbose_name_plural = 'Tipos de Ovinos/Caprinos'
        
    def __unicode__(self):
        return self.tipo
        
        
class OvinoCaprino(AnimalTerrestre):
    
    tipoOvinoCaprino = models.ForeignKey(TipoOvinoCaprino,verbose_name='Tipo de Ovino/Caprino')
    
    class Meta:
        verbose_name = 'Ovino/Caprino'
        verbose_name_plural = 'Ovinos/Caprinos'
        
        
class TipoProdutoOvinocaprinocultura(TipoProdutoAnimal):
    
    class Meta:
        verbose_name = 'Tipo Produto Ovinocaprinocultura'
        verbose_name_plural = 'Tipos Produto Ovinocaprinocultura'
        

class Ovinocaprinocultura(ProdutoUnidadeProducao):
    
    class Meta:
        verbose_name = 'Ovinocaprinocultura'
        verbose_name_plural = 'Ovinocaprinocultura'
        

class ProdutoOvinocaprinocultura(ProdutoAnimal):
    
    ovinoaprinocultura = models.ForeignKey(Ovinocaprinocultura,verbose_name='Ovinocaprinocultura')
    tipoProdutoOvinoCaprino = models.ForeignKey(TipoProdutoOvinocaprinocultura,verbose_name='Tipo Produto')     

    class Meta:
        verbose_name = 'Produto Ovinocabrinocultura'
        verbose_name_plural = 'Produtos Ovinocabrinocultura'
        
        
#Aves

class TipoAve(models.Model):
    
    tipo = models.CharField('Tipo de Ave',max_length=16)
    
    class Meta:
        verbose_name = 'Tipo de Ave'
        verbose_name_plural = 'Tipos de Aves'
        
    def __unicode__(self):
        return self.tipo
        
        
class Ave(AnimalTerrestre):
    
    tipoAve = models.ForeignKey(TipoAve,verbose_name='Tipo de Ave')
    
    class Meta:
        verbose_name = 'Ave'
        verbose_name_plural = 'Aves'
        

class TipoProdutoAvicultura(TipoProdutoAnimal):
    
    class Meta:
        verbose_name = 'Tipo Produto Ave'
        verbose_name_plural = 'Tipos Produto Ave'
        

class Avicultura(ProdutoUnidadeProducao):
    
    class Meta:
        verbose_name = 'Avicultura'
        verbose_name_plural = 'Avicultura'
        

class ProdutoAvicultura(ProdutoAnimal):
    
    avicultura = models.ForeignKey(Avicultura,verbose_name='Avicultura')
    tipoProdutoAve = models.ForeignKey(TipoProdutoAvicultura,verbose_name='Tipo Produto')     

    class Meta:
        verbose_name = 'Produto Avicultura'
        verbose_name_plural = 'Produtos Avicultura'


#Apicultura

class Abelha(models.Model):
    
    unidadeProducao = models.ForeignKey(UnidadeProducao,verbose_name='Unidade de Produção')
    tipo = models.CharField('Tipo',max_length=16)
    quantidade = models.IntegerField('Quantidade')
    modeloColmeia = models.CharField('Modelo Colméia',max_length=16)
    especie = models.CharField('Espécie',max_length=16)
    valorUnitario = models.DecimalField('Valor Unitário',max_digits=8,decimal_places=2)
    localizacao = models.CharField('Localização',max_length=32,blank=True)
    
    class Meta:
        verbose_name = 'Apicultura'
        verbose_name_plural = 'Apiculturas'
        
    def valorTotal(self):
        return self.quantidade * self.valorUnitario
        

class TipoProdutoApicultura(TipoProdutoAnimal):
    
    class Meta:
        verbose_name = 'Tipo Produto Apicultura'
        verbose_name_plural = 'Tipos Produto Apicultura'
        

class Apicultura(ProdutoUnidadeProducao):
    
    class Meta:
        verbose_name = 'Apicultura'
        verbose_name_plural = 'Apicultura'
        

class ProdutoApicultura(ProdutoAnimal):
    
    apicultura = models.ForeignKey(Apicultura,verbose_name='Apicultura')
    tipoProdutoApicultura = models.ForeignKey(TipoProdutoApicultura,verbose_name='Tipo Produto')     

    class Meta:
        verbose_name = 'Produto Apicultura'
        verbose_name_plural = 'Produtos Apicultura'
        

#Outros - ????

#class Outros(models.Model):
    
#    unidadeProducao = models.ForeignKey(UnidadeProducao,verbose_name='Unidade de Produção')
#    unidade = models.CharField('Unidade',max_length=16)
#    especie = models.CharField('Espécie',max_length=16)
#    quantidade = models.DecimalField('Quantidade(ha)',max_digits=8,decimal_places=2)
#    valorUnitario = models.DecimalField('Valor Unitário',max_digits=8,decimal_places=2)
#    localizacao = models.CharField('Localização',max_length=32)
    
#    class Meta:
#        verbose_name = 'Outra Cultura Animal'
#        verbose_name_plural = 'Outras Culturas Animais'

#Psicultura

class Peixe(models.Model):
    
    SISTEMA_PRODUCAO = (
        ('Intensivo', 'Intensivo'),
        ('Semi-intensivo', 'Semi-intensivo'),
        ('Extensivo', 'Extensivo'),
    )
    
    unidadeProducao = models.ForeignKey(UnidadeProducao,verbose_name='Unidade de Produção')
    unidade = models.CharField('Unidade',max_length=16)
    especie = models.CharField('Espécie',max_length=16)
    quantidade = models.DecimalField('Quantidade(ha)',max_digits=8,decimal_places=2)
    valorUnitario = models.DecimalField('Valor Unitário',max_digits=8,decimal_places=2)
    localizacao = models.CharField('Localização',max_length=32,blank=True)
    sistemaProducao = models.CharField('Sistema de Produção',max_length=16,choices=SISTEMA_PRODUCAO)
    
    class Meta:
        verbose_name = 'Pscicultura'
        verbose_name_plural = 'Psciculturas'
        
    def valorTotal(self):
        return self.quantidade * self.valorUnitario
        
        
class TipoProdutoPscicultura(TipoProdutoAnimal):
    
    class Meta:
        verbose_name = 'Tipo Produto Pscicultura'
        verbose_name_plural = 'Tipos Produto Pscicultura'
        

class Pscicultura(ProdutoUnidadeProducao):
    
    class Meta:
        verbose_name = 'Pscicultura'
        verbose_name_plural = 'Pscicultura' 
        

class ProdutoPscicultura(ProdutoAnimal):
    
    pscicultura = models.ForeignKey(Pscicultura,verbose_name='Pscicultura')
    tipoProdutoPsicultura = models.ForeignKey(TipoProdutoPscicultura,verbose_name='Tipo Produto')     

    class Meta:
        verbose_name = 'Produto Pscicultura'
        verbose_name_plural = 'Produtos Pscicultura'
        
        
#Culturas Agrícolas

class TipoCultura(models.Model):
    
    UNIDADE_MEDIDA_CULTURA = (
        ('Sc', 'Sc'),
        ('t', 't'),
        ('@', '@'),
        ('Kg', 'Kg'),
        ('m³', 'm³')
    )
    
    tipo = models.CharField('Tipo de Cultura',max_length=32)
    UnidadeMedida = models.CharField('Unidade de Medida',max_length=8,choices=UNIDADE_MEDIDA_CULTURA)
    
    class Meta:
        verbose_name = 'Tipo de Cultura'
        verbose_name_plural = 'Tipos de Cultura'   
        
    def __unicode__(self):
        return self.tipo    
     

class Agricultura(ProdutoUnidadeProducao):
    
    class Meta:
        verbose_name = 'Agricultura'
        verbose_name_plural = 'Agricultura'  
            
      
class SistemaCultura(models.Model):
    
    sistema = models.CharField('Sistema de Cultura',max_length=32)
     
    class Meta:
        verbose_name = 'Sistema de Cultura'
        verbose_name_plural = 'Sistemas de Cultura'
    
    def __unicode__(self):
        return self.sistema
        
        
class ProdutoAgricola(Produto):
    
    agricultura = models.ForeignKey(Agricultura,verbose_name='Agricultura')
    tipoCultura = models.ForeignKey(TipoCultura,verbose_name='Tipo de Cultura')
    sistemaCultura = models.ForeignKey(SistemaCultura,verbose_name='Sistema de Cultura')
    areaPlantada = models.DecimalField('Área Plantada(ha)',max_digits=8,decimal_places=2)
    produto = models.CharField('Produto',max_length=16)
    producaoEstimada = models.DecimalField('Produção Estimada',max_digits=8,decimal_places=2)
    
    class Meta:
        verbose_name = 'Produto Agrícola'
        verbose_name_plural = 'Produtos Agrícolas'
        
    def valorTotal(self):
        return self.producaoEstimada * self.valorUnitario
        

#Culturas Extrativistas

class TipoExtrativismo(models.Model):
    
    UNIDADE_MEDIDA_EXTRATIVISMO = (
        ('M3', 'M³'),
    )
    
    tipo = models.CharField('Tipo de Extrativismo',max_length=16)
    UnidadeMedida = models.CharField('Unidade de Medida',max_length=8,choices=UNIDADE_MEDIDA_EXTRATIVISMO)
    
    class Meta:
        verbose_name = 'Tipo de Extrativismo'
        verbose_name_plural = 'Tipos de Extrativismo'   
        
    def __unicode__(self):
        return self.tipo 
    
    
class Extrativismo(ProdutoUnidadeProducao):
    
    class Meta:
        verbose_name = 'Extrativismo'
        verbose_name_plural = 'Extrativismo'
        
    
class ProdutoExtrativismo(Produto):
    
    extrativismo = models.ForeignKey(Extrativismo,verbose_name='Extrativismo')
    tipoExtrativismo = models.ForeignKey(TipoExtrativismo,verbose_name='Tipo de Extrativismo')
    areaManejada = models.DecimalField('Área Manejada(ha)',max_digits=8,decimal_places=2)
    produto = models.CharField('Produto',max_length=16)
    producaoEstimada = models.DecimalField('Produção Estimada',max_digits=8,decimal_places=2)
    
    class Meta:
        verbose_name = 'Produto Extrativismo'
        verbose_name_plural = 'Produtos Extrativismo'
        
    def valorTotal(self):
        return self.producaoEstimada * self.valorUnitario

#Rendas de Fora da Propriedade

class RendaForaPropriedade(models.Model):
    
    FREQUENCIA = (
        ('Anual', 'Anual'),
        ('Mensal', 'Mensal'),
        ('Semanal', 'Semanal'),
    )
    
    beneficiario = models.ForeignKey(Beneficiario,verbose_name='Beneficiário')
    nome = models.CharField('Nome Pessoa',max_length=64)
    atividade = models.CharField('Atividade',max_length=32)
    valor = models.DecimalField('Valor',max_digits=8,decimal_places=2)
    frequencia = models.CharField('Frequência',max_length=8,choices=FREQUENCIA)
    
    class Meta:
        verbose_name = 'Renda de Fora da Propriedade'
        verbose_name_plural = 'Rendas de Fora da Propriedade'
        
    def __unicode__(self):
        return self.nome
        
        
#Rendas de Fora da Agricultura

class RendaForaAgricultura(models.Model):
    
    beneficiario = models.ForeignKey(Beneficiario,verbose_name='Beneficiário')
    nome = models.CharField('Nome Pessoa',max_length=32)
    atividade = models.CharField('Atividade',max_length=32)
    receita = models.DecimalField('Receita',max_digits=8,decimal_places=2)
    custo = models.DecimalField('Custo',max_digits=8,decimal_places=2)
    
    class Meta:
        verbose_name = 'Renda de Fora da Agricultura'
        verbose_name_plural = 'Rendas de Fora da Agricultura'
        
    def __unicode__(self):
        return self.nome
        
        
#Comercialização

class TipoComercializacao(models.Model):
    
    forma = models.CharField('Forma de Comercialização',max_length=16)
    
    class Meta:
        verbose_name = 'Forma de Comercialização'
        verbose_name_plural = 'Forma de Comercialização'
        
    def __unicode__(self):
        return self.forma


class Comercializacao(ProdutoUnidadeProducao):
    
    class Meta:
        verbose_name = 'Comercialização'
        verbose_name_plural = 'Comercialização'
           

class ProdutoComercializacao(models.Model):
    
    comercializacao = models.ForeignKey(Comercializacao,verbose_name='Comercialização')
    forma = models.ForeignKey(TipoComercializacao,verbose_name='Forma')
    produto = models.CharField('Produto',max_length=16)
    quantidade = models.DecimalField('Quantidade',max_digits=8,decimal_places=2)
    renda = models.DecimalField('Renda',max_digits=8,decimal_places=2)
    
    class Meta:
        verbose_name = 'Produto Comercialização'
        verbose_name_plural = 'Protudo Comercialização'
        

#Acesso a Políticas Públicas

class PoliticaPublica(models.Model):
    
    politicasPublicas = models.ManyToManyField(Beneficiario, through='PoliticaPublica_Beneficiario')
    politicaPublica = models.CharField('Política Pública',max_length=32)
    
    class Meta:
        verbose_name = 'Política Pública'
        verbose_name_plural = 'Políticas Públicas'
        
    def __unicode__(self):
        return self.politicaPublica
    
    
class PoliticaPublica_Beneficiario(models.Model):
    
    SITUACAO = (
        ('Pago', 'Pago'),
        ('Andamento', 'Andamento'),
    )
    
    politicaPublica = models.ForeignKey(PoliticaPublica,verbose_name='Política Pública')
    beneficiario = models.ForeignKey(Beneficiario,verbose_name='Beneficiário')
    linha = models.CharField('Linha',max_length=16,blank=True)
    modalidade = models.CharField('Modalidade',max_length=16,blank=True)
    valor = models.DecimalField('Valor',max_digits=8,decimal_places=2,blank=True,null=True)
    situacao = models.CharField('Situação',max_length=16,choices=SITUACAO,blank=True)
    destino = models.CharField('Destino',max_length=16,blank=True)
    anoAcesso = models.CharField('Ano de Acesso',max_length=4,blank=True)
    entidade = models.CharField('Entidade',max_length=16,blank=True)
    renegociacao = models.BooleanField('Renegociação',blank=True)
           
    class Meta:
        verbose_name = 'Acesso a Política Pública'
        verbose_name_plural = 'Acesso a Políticas Públicas'    
        
        
#Organização Social

class OrganizacaoSocial(models.Model):
    
    entidade = models.CharField('Entidade',max_length=32)
    entidades = models.ManyToManyField(Beneficiario, through='OrganizacaoSocial_Beneficiario')

    class Meta:
        verbose_name = 'Organização Social'
        verbose_name_plural = 'Organizações Sociais'
        
    def __unicode__(self):
        return self.entidade
        

class OrganizacaoSocial_Beneficiario(models.Model):
    
    FREQUENCIA = (
        ('Anual', 'Anual'),
        ('Semestral', 'Semestral'),
        ('Mensal', 'Mensal'),
        ('Semanal', 'Semanal'),
    )
    
    organizacaoSocial = models.ForeignKey(OrganizacaoSocial,verbose_name='Organização Social')
    beneficiario = models.ForeignKey(Beneficiario,verbose_name='Beneficiário')
    frequencia = models.CharField('Frequência',max_length=16,choices=FREQUENCIA)
    emDia = models.BooleanField('Em dia')
    
    class Meta:
        verbose_name = 'Participação em Organização Social'
        verbose_name_plural = 'Participações em Organizações Sociais'