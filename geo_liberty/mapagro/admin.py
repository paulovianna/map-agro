# -*- coding: utf-8 -*-
from django.contrib.gis import admin
from models import *

class AdminGeo(admin.OSMGeoAdmin):
    
    scrollable = True
    map_width = 700
    map_height = 350
    
#Beneficiario    
admin.site.register(Beneficiario)
admin.site.register(Familia)

#Informações Gerais Unidade de Produção
admin.site.register(DestinoLixo)
admin.site.register(Agrotoxico)
admin.site.register(DestinoEmbalagemAgrotoxico)
admin.site.register(PreparoSolo)
admin.site.register(InsumosOrganicos)
admin.site.register(UtilizacaoArvores)
admin.site.register(PraticaConservacaoSolo)

#Unidade de Produção
admin.site.register(UnidadeProducao,AdminGeo)
admin.site.register(Confrontacao)
admin.site.register(Terra)
admin.site.register(Terra_UnidadeProducao)
admin.site.register(Benfeitoria)
admin.site.register(Benfeitoria_UnidadeProducao)
admin.site.register(EquipamentoTrabalho)
admin.site.register(EquipamentoTrabalho_UnidadeProducao)

#Bovinos
admin.site.register(TipoBovino)
admin.site.register(Bovino)
admin.site.register(TipoProdutoBovino)
admin.site.register(ProdutoBovino)

#Suino
admin.site.register(TipoSuino)
admin.site.register(Suino)
admin.site.register(TipoProdutoSuino)
admin.site.register(ProdutoSuino)

#Ovino/Caprino
admin.site.register(TipoOvinoCaprino)
admin.site.register(OvinoCaprino)
admin.site.register(TipoProdutoOvinoCaprino)
admin.site.register(ProdutoOvinoCaprino)

#Aves
admin.site.register(TipoAve)
admin.site.register(Ave)
admin.site.register(TipoProdutoAve)
admin.site.register(ProdutoAve)

#Apicultura
admin.site.register(TipoProdutoApicultura)
admin.site.register(Apicultura)
admin.site.register(ProdutoApicultura)

#Psicultura
admin.site.register(TipoProdutoPsicultura)
admin.site.register(Psicultura)
admin.site.register(ProdutoPsicultura)

#Outros ???
#admin.site.register(Outros)

#Culturas
admin.site.register(TipoCultura)
admin.site.register(Cultura)

#Renda de Fora da Propriedade
admin.site.register(RendaForaPropriedade)

#Renda de Fora da Agricultura
admin.site.register(RendaForaAgricultura)

#Comercialização
admin.site.register(TipoComercializacao)
admin.site.register(Comercializacao)

#Acesso a Políticas Públicas
admin.site.register(PoliticaPublica)
admin.site.register(PoliticaPublica_UnidadeProducao)

#Organização Social
admin.site.register(OrganizacaoSocial)
admin.site.register(OrganizacaoSocial_UnidadeProducao)