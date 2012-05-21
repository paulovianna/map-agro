# -*- coding: utf-8 -*-
from django.contrib.gis.db import models
from smart_selects.db_fields import *
from geo_liberty.models import PessoaFisica,Ponto,Municipio

#Classes Abstratas

class Proprietario(PessoaFisica):
    
    OPCOES_ESTADO_CIVIL = (
        ('Casado', 'Casado'),
        ('Solteiro', 'Solteiro'),
    )
    
    municipio = models.ForeignKey(Municipio,verbose_name='Município')
    rg = models.CharField('RG',max_length=16)
    telefone = models.CharField('Telefone',max_length=16)
    endereco = models.CharField('Endereço',max_length=32)
    estadoCivil = models.CharField('Estado Civil',max_length=8,choices=OPCOES_ESTADO_CIVIL)
    
    class Meta:
        abstract = True 
        
    
class Propriedade(Ponto):
    
    municipio = models.ForeignKey(Municipio,verbose_name='Município')
    denominacao = models.CharField('Denominação',max_length=32)
    localizacao = models.CharField('Localização',max_length=32)
    area = models.FloatField('Área')
    
    class Meta:
        abstract = True 
    
    def __unicode__(self):
        return self.denominacao
      
          
#Beneficiário
        
class Beneficiario(Proprietario):
    
    CLASSIFICACAO = (
        ('Quilombola', 'Quilombola'),
        ('Extrativista', 'Extrativista'),
        ('Ribeirinho', 'Ribeirinho'),
        ('Assentado', 'Assentado'),
    )
    
    dap = models.CharField('Nº DAP',max_length=2)
    situacao = models.CharField('Situação',max_length=16)
    classificacao = models.CharField('Classificação',max_length=16,choices=CLASSIFICACAO)

    class Meta:
        verbose_name = 'Beneficiário'
        verbose_name_plural = 'Beneficiários'
        

class Familia(PessoaFisica):
    
    parentesco = models.CharField('Parentesco',max_length=16)
    dap = models.CharField('Nº DAP',max_length=2)
    beneficiario = models.ForeignKey(Beneficiario,verbose_name='Beneficiario')

    class Meta:
        verbose_name = 'Membro da Família'
        verbose_name_plural = 'Membros da Família'
        

#Informações Gerais Unidade de Produção

class DestinoLixo(models.Model):
    
    TIPO_LIXO = (
        ('Orgânico', 'Orgânico'),
        ('Inorgânico', 'Inorgânico'),
    )
    
    destino = models.CharField('Destino do Lixo',max_length=16)
    tipoLixo = models.CharField('Tipo Lixo',max_length=16,choices=TIPO_LIXO)
     
    class Meta:
        verbose_name = 'Destino do Lixo'
        verbose_name_plural = 'Destinos do Lixo'
        
    def __unicode__(self):
        return self.destino
        

class Agrotoxico(models.Model):
    
    agrotoxico = models.CharField('Agrotóxico',max_length=16)
    
    class Meta:
        verbose_name = 'Agrotóxico'
        verbose_name_plural = 'Agrotóxicos'
        
    def __unicode__(self):
        return self.agrotoxico
        
        
class DestinoEmbalagemAgrotoxico(models.Model):
    
    destino = models.CharField('Destino de Embalagem de Agrotóxico',max_length=16)
    
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
    
    insumoOrganico = models.CharField('Insumo Orgânico',max_length=16)
    
    class Meta:
        verbose_name = 'Insumo Orgânico'
        verbose_name_plural = 'Insumos Orgânicos'
        
    def __unicode__(self):
        return self.insumoOrganico


class UtilizacaoArvores(models.Model):
    
    utilizacaoArvore = models.CharField('Utilização de Árvores',max_length=16)
    
    class Meta:
        verbose_name = 'Utilização de Árvore'
        verbose_name_plural = 'Utilizações de Árvore'
        
    def __unicode__(self):
        return self.utilizacaoArvore
    
        
class PraticaConservacaoSolo(models.Model):
    
    conservacaoSolo = models.CharField('Prática de Conservação do Solo',max_length=16)
    
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
    
    beneficiario = models.ForeignKey(Beneficiario,verbose_name='Beneficiário')
    participacao = models.DecimalField('Participação %',max_digits=8,decimal_places=2)
    tituloDominio = models.CharField('Título de Domínio',max_length=16)
    dataRegistro = models.DateField('Data de Registro')
    registro = models.CharField('Registro',max_length=16)
    receitaFederal = models.CharField('Nº Receita Federal (ITR)',max_length=16)
    qualidadeAgua = models.CharField('Qualidade da Água',max_length=8,choices=QUALIDADE_AGUA,blank=True)
    destinoLixo = models.ManyToManyField(DestinoLixo,verbose_name='Destino do Lixo',blank=True)
    utilizacaoAgrotoxico = models.ManyToManyField(Agrotoxico,verbose_name='Utilização de Agrotóxicos',blank=True)
    destinoEmbalagemAgrotoxico = models.ManyToManyField(DestinoEmbalagemAgrotoxico,verbose_name='Destino da Embalagem de Agrotóxico',blank=True)
    preparoSolo = models.ManyToManyField(PreparoSolo,verbose_name='Preparo do Solo',blank=True)
    areaErosao = models.DecimalField('Área com Erosão',max_digits=8,decimal_places=2,blank=True)
    praticaConservacaoSolo = models.ManyToManyField(PraticaConservacaoSolo,verbose_name='Pratica de Conservação do Solo',blank=True)
    insumosOrganicos = models.ManyToManyField(InsumosOrganicos,verbose_name='Insumos Orgânicos',blank=True)
    rotacaoCultura = models.BooleanField('Rotação de Cultura',blank=True)
    utilizacaoArvores = models.ManyToManyField(UtilizacaoArvores,verbose_name='Utilização de Árvores',blank=True)
    
    class Meta:
        verbose_name = 'Unidade de Produção Familiar'
        verbose_name_plural = 'Unidades de Produção Familiar'
    

class Confrontacao(models.Model):
    
    unidadeProducao = models.ForeignKey(UnidadeProducao,verbose_name='Unidade de Produção Familiar')
    norte = models.CharField('Norte',max_length=8)
    sul = models.CharField('Sul',max_length=8)
    leste = models.CharField('Leste',max_length=8)
    oeste = models.CharField('Oeste',max_length=8)
    roteiroAcesso = models.TextField('Roteiro de Acesso')
    
    class Meta:
        verbose_name = 'Confrontação'
        verbose_name_plural = 'Confrontações'
        
    def __unicode__(self):
        return self.unidadeProducao
    
    
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
        

class Benfeitoria(models.Model):
    
    UNIDADE = (
        ('M³', 'M³'),
        ('M²', 'M²'),
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
    quantidade = models.DecimalField('Área',max_digits=3,decimal_places=2)
    valorUnitario = models.DecimalField('Valor Unitário',max_digits=8,decimal_places=2)
    obervacoes = models.TextField('Observações')
    
    class Meta:
        verbose_name = 'Benfeitoria de Unidade de Produção'
        verbose_name_plural = 'Benfeitorias de Unidade de Produção'


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
    capacidadePotencia = models.CharField('Capacidade / Potência',max_length=8)
    mediaIdade = models.IntegerField('Média de Idade(anos)')
    
    class Meta:
        verbose_name = 'Equipamento de Trabalho de Unidade de Produção'
        verbose_name_plural = 'Equipamentos de Trabalho de Unidade de Produção'


#Classes Abstratas para Bovinos,Suinos,Caprinos,Aves

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
    localizacao = models.CharField('Localização',max_length=32)
    
    class Meta:
        abstract = True
        

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
        

class ProdutoAnimal(models.Model):
    
    quantidade = models.IntegerField('Quantidade')
    valorUnitario = models.DecimalField('Valor Unitário',max_digits=8,decimal_places=2)
            
    class Meta:
        abstract = True
         
        
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
        
        
class TipoProdutoBovino(TipoProdutoAnimal):
    
    class Meta:
        verbose_name = 'Tipo Produto Bovino'
        verbose_name_plural = 'Tipos Produto Bovino'
        

class ProdutoBovino(ProdutoAnimal):
    
    bovino = models.ForeignKey(Bovino,verbose_name='Bovino')
    tipoProdutoBovino = models.ForeignKey(TipoProdutoBovino,verbose_name='Tipo Produto')     

    class Meta:
        verbose_name = 'Produto Bovino'
        verbose_name_plural = 'Produtos Bovinos'
        
        
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
        

class TipoProdutoSuino(TipoProdutoAnimal):
    
    class Meta:
        verbose_name = 'Tipo Produto Suíno'
        verbose_name_plural = 'Tipos Produto Suíno'
        

class ProdutoSuino(ProdutoAnimal):
    
    suino = models.ForeignKey(Suino,verbose_name='Suíno')
    tipoProdutoSuino = models.ForeignKey(TipoProdutoSuino,verbose_name='Tipo Produto')     

    class Meta:
        verbose_name = 'Produto Suíno'
        verbose_name_plural = 'Produtos Suínos'
        
        
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
        
        
class TipoProdutoOvinoCaprino(TipoProdutoAnimal):
    
    class Meta:
        verbose_name = 'Tipo Produto Ovino/Caprino'
        verbose_name_plural = 'Tipos Produto Ovino/Caprino'
        

class ProdutoOvinoCaprino(ProdutoAnimal):
    
    ovinoCaprino = models.ForeignKey(OvinoCaprino,verbose_name='Ovino/Caprino')
    tipoProdutoOvinoCaprino = models.ForeignKey(TipoProdutoOvinoCaprino,verbose_name='Tipo Produto')     

    class Meta:
        verbose_name = 'Produto Ovino/Caprino'
        verbose_name_plural = 'Produtos Ovino/Caprinos'
        
        
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
        

class TipoProdutoAve(TipoProdutoAnimal):
    
    class Meta:
        verbose_name = 'Tipo Produto Ave'
        verbose_name_plural = 'Tipos Produto Ave'
        

class ProdutoAve(ProdutoAnimal):
    
    ave = models.ForeignKey(Ave,verbose_name='Ave')
    tipoProdutoAve = models.ForeignKey(TipoProdutoAve,verbose_name='Tipo Produto')     

    class Meta:
        verbose_name = 'Produto Ave'
        verbose_name_plural = 'Produtos Aves'


#Apicultura

class Apicultura(models.Model):
    
    unidadeProducao = models.ForeignKey(UnidadeProducao,verbose_name='Unidade de Produção')
    tipo = models.CharField('Tipo',max_length=16)
    quantidade = models.IntegerField('Quantidade')
    modeloColmeia = models.CharField('Modelo Colméia',max_length=16)
    especie = models.CharField('Espécie',max_length=16)
    valorUnitario = models.DecimalField('Valor Unitário',max_digits=8,decimal_places=2)
    localizacao = models.CharField('Localização',max_length=32)
    
    class Meta:
        verbose_name = 'Apicultura'
        verbose_name_plural = 'Apiculturas'
        

class TipoProdutoApicultura(TipoProdutoAnimal):
    
    class Meta:
        verbose_name = 'Tipo Produto Apicultura'
        verbose_name_plural = 'Tipos Produto Apicultura'
        

class ProdutoApicultura(ProdutoAnimal):
    
    apicultura = models.ForeignKey(Apicultura,verbose_name='Apicultura')
    tipoProdutoApicultura = models.ForeignKey(TipoProdutoApicultura,verbose_name='Tipo Produto')     

    class Meta:
        verbose_name = 'Produto Apicultura'
        verbose_name_plural = 'Produtos Apicultura'
        

#Outros - ????

class Outros(models.Model):
    
    unidadeProducao = models.ForeignKey(UnidadeProducao,verbose_name='Unidade de Produção')
    unidade = models.CharField('Unidade',max_length=16)
    especie = models.CharField('Espécie',max_length=16)
    quantidade = models.DecimalField('Quantidade(ha)',max_digits=8,decimal_places=2)
    valorUnitario = models.DecimalField('Valor Unitário',max_digits=8,decimal_places=2)
    localizacao = models.CharField('Localização',max_length=32)
    
    class Meta:
        verbose_name = 'Outra Cultura Animal'
        verbose_name_plural = 'Outras Culturas Animais'

#Psicultura

class Psicultura(Outros):
    
    SISTEMA_PRODUCAO = (
        ('Intensivo', 'Intensivo'),
        ('Semi-intensivo', 'Semi-intensivo'),
        ('Extensivo', 'Extensivo'),
    )
    
    sistemaProducao = models.CharField('Sistema de Produção',max_length=16,choices=SISTEMA_PRODUCAO)
    
    class Meta:
        verbose_name = 'Psicultura'
        verbose_name_plural = 'Psiculturas'
        
        
class TipoProdutoPsicultura(TipoProdutoAnimal):
    
    class Meta:
        verbose_name = 'Tipo Produto Psicultura'
        verbose_name_plural = 'Tipos Produto Psicultura'
        

class ProdutoPsicultura(ProdutoAnimal):
    
    psicultura = models.ForeignKey(Psicultura,verbose_name='Psicultura')
    tipoProdutoPsicultura = models.ForeignKey(TipoProdutoPsicultura,verbose_name='Tipo Produto')     

    class Meta:
        verbose_name = 'Produto Psicultura'
        verbose_name_plural = 'Produtos Psicultura'
        
        
#Culturas

class TipoCultura(models.Model):
    
    UNIDADE_MEDIDA_CULTURA = (
        ('Sc', 'Sc'),
        ('t', 't'),
        ('@', '@'),
    )
    
    tipo = models.CharField('Tipo de Cultura',max_length=16)
    UnidadeMedida = models.CharField('Unidade de Medida',max_length=8,choices=UNIDADE_MEDIDA_CULTURA)
    
    class Meta:
        verbose_name = 'Tipo de Cultura'
        verbose_name_plural = 'Tipos de Cultura'   
        
    def __unicode__(self):
        return self.tipo     
        
        
class Cultura(models.Model):   
    
    SISTEMA_CULTURA = (
        ('Monocultivo', 'Monocultivo'),
        ('Policultivo', 'Policultivo'),
        ('Lavoura/Pecuária', 'Lavoura/Pecuária'),
    )
    
    unidadeProducao = models.ForeignKey(UnidadeProducao,verbose_name='Unidade de Produção')
    tipoCultura = models.ForeignKey(TipoCultura,verbose_name='Tipo de Cultura')
    sistemaCultura = models.CharField('Sistema de Cultura',max_length=16,choices=SISTEMA_CULTURA)
    areaPlantada = models.DecimalField('Área Plantada(ha)',max_digits=8,decimal_places=2)
    produto = models.CharField('Produto',max_length=16)
    producaoEstimada = models.DecimalField('Produção Estimada',max_digits=8,decimal_places=2)
    valorUnitario = models.DecimalField('Valor Unitário',max_digits=8,decimal_places=2)
    
    class Meta:
        verbose_name = 'Cultura'
        verbose_name_plural = 'Culturas'
    

#Rendas de Fora da Propriedade

class RendaForaPropriedade(models.Model):
    
    FREQUENCIA = (
        ('Anual', 'Anual'),
        ('Mensal', 'Mensal'),
        ('Semanal', 'Semanal'),
    )
    
    beneficiario = models.ForeignKey(Beneficiario,verbose_name='Beneficiário')
    nome = models.CharField('Nome',max_length=64)
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
    nome = models.CharField('Nome',max_length=32)
    atividade = models.CharField('Atividade',max_length=32)
    receita = models.DecimalField('Receita',max_digits=8,decimal_places=2)
    custo = models.DecimalField('Custo',max_digits=8,decimal_places=2)
    
    class Meta:
        verbose_name = 'Renda de Fora da Agricultura'
        verbose_name_plural = 'Rendas de Fora da Agricultura'
        
    def __unicode__(self):
        return self.familia
        
        
#Comercialização

class TipoComercializacao(models.Model):
    
    forma = models.CharField('Forma de Comercialização',max_length=16)
    
    class Meta:
        verbose_name = 'Forma de Comercialização'
        verbose_name_plural = 'Forma de Comercialização'
        
    def __unicode__(self):
        return self.forma
    

class Comercializacao(models.Model):
    
    forma = models.ForeignKey(TipoComercializacao,verbose_name='Forma')
    produto = models.CharField('Produto',max_length=16)
    quantidade = models.DecimalField('Quantidade',max_digits=8,decimal_places=2)
    renda = models.DecimalField('Renda',max_digits=8,decimal_places=2)
    
    class Meta:
        verbose_name = 'Comercialização'
        verbose_name_plural = 'Comercializações'
        

#Acesso a Políticas Públicas

class PoliticaPublica(models.Model):
    
    politicasPublicas = models.ManyToManyField(Beneficiario, through='PoliticaPublica_Beneficiario')
    politicaPublica = models.CharField('Política Pública',max_length=16)
    
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
    linha = models.CharField('Linha',max_length=16)
    modalidade = models.CharField('Modalidade',max_length=16)
    valor = models.DecimalField('Valor',max_digits=8,decimal_places=2)
    situacao = models.CharField('Situação',max_length=16,choices=SITUACAO)
    destino = models.CharField('Destino',max_length=16)
    anoAcesso = models.CharField('Ano de Acesso',max_length=4)
    entidade = models.CharField('Entidade',max_length=16)
    renegociacao = models.BooleanField('Renegociação')
           
    class Meta:
        verbose_name = 'Acesso a Política Pública'
        verbose_name_plural = 'Acesso a Políticas Públicas'    
        
        
#Organização Social

class OrganizacaoSocial(models.Model):
    
    entidade = models.CharField('Entidade',max_length=16)
    entidades = models.ManyToManyField(Beneficiario, through='OrganizacaoSocial_Beneficiario')

    class Meta:
        verbose_name = 'Organização Social'
        verbose_name_plural = 'Organizações Sociais'
        
    def __unicode__(self):
        return self.entidade
        

class OrganizacaoSocial_Beneficiario(models.Model):
    
    FREQUENCIA = (
        ('Anual', 'Anual'),
        ('Mensal', 'Mensal'),
        ('Semanal', 'Semanal'),
    )
    
    organizacaoSocial = models.ForeignKey(OrganizacaoSocial,verbose_name='Organização Social')
    beneficiario = models.ForeignKey(Beneficiario,verbose_name='Beneficiário')
    frequencia = models.CharField('Frequência',max_length=8,choices=FREQUENCIA)
    emDia = models.BooleanField('Em dia')
    
    class Meta:
        verbose_name = 'Participação em Organização Social'
        verbose_name_plural = 'Participações em Organizações Sociais'