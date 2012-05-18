# -*- coding: utf-8 -*-
from django.contrib.gis import admin
from models import *

#Classe Model Ojetos Geográficos
class AdminGeo(admin.OSMGeoAdmin):
    
    scrollable = True
    map_width = 700
    map_height = 350
    
#Classe Ocultar Model Index Admin   
class OcultarAdmin(admin.ModelAdmin):
    
    def get_model_perms(self, request):
        return {}
       
#Beneficiario 
class AdminBeneficiario(admin.ModelAdmin):
    pass
   
admin.site.register(Beneficiario,AdminBeneficiario)
admin.site.register(Familia)

#Informações Gerais Unidade de Produção
class AdminDestinoLixo(OcultarAdmin):
    pass

class AdminAgrotoxico(OcultarAdmin):
    pass

class AdminDestinoEmbalagemAgrotoxico(OcultarAdmin):
    pass

class AdminPreparoSolo(OcultarAdmin):
    pass

class AdminInsumosOrganicos(OcultarAdmin):
    pass

class AdminUtilizacaoArvores(OcultarAdmin):
    pass

class AdminPraticaConservacaoSolo(OcultarAdmin):
    pass

admin.site.register(DestinoLixo,AdminDestinoLixo)
admin.site.register(Agrotoxico,AdminAgrotoxico)
admin.site.register(DestinoEmbalagemAgrotoxico,AdminDestinoEmbalagemAgrotoxico)
admin.site.register(PreparoSolo,AdminPreparoSolo)
admin.site.register(InsumosOrganicos,AdminInsumosOrganicos)
admin.site.register(UtilizacaoArvores,AdminUtilizacaoArvores)
admin.site.register(PraticaConservacaoSolo,AdminPraticaConservacaoSolo)

#Unidade de Produção
class AdminTerra(OcultarAdmin):
    pass

class AdminBenfeitoria(OcultarAdmin):
    pass

class AdminEquipamentoTrabalho(OcultarAdmin):
    pass

admin.site.register(UnidadeProducao,AdminGeo)
admin.site.register(Confrontacao)
admin.site.register(Terra,AdminTerra)
admin.site.register(Terra_UnidadeProducao)
admin.site.register(Benfeitoria,AdminBenfeitoria)
admin.site.register(Benfeitoria_UnidadeProducao)
admin.site.register(EquipamentoTrabalho,AdminEquipamentoTrabalho)
admin.site.register(EquipamentoTrabalho_UnidadeProducao)

#Bovinos
class AdminTipoBovino(OcultarAdmin):
    pass

class AdminTipoProdutoBovino(OcultarAdmin):
    pass

admin.site.register(TipoBovino,AdminTipoBovino)
admin.site.register(Bovino)
admin.site.register(TipoProdutoBovino,AdminTipoProdutoBovino)
admin.site.register(ProdutoBovino)

#Suino
class AdminTipoSuino(OcultarAdmin):
    pass

class AdminTipoProdutoSuino(OcultarAdmin):
    pass

admin.site.register(TipoSuino,AdminTipoSuino)
admin.site.register(Suino)
admin.site.register(TipoProdutoSuino,AdminTipoProdutoSuino)
admin.site.register(ProdutoSuino)

#Ovino/Caprino
class AdminTipoOvinoCaprino(OcultarAdmin):
    pass

class AdminTipoProdutoOvinoCaprino(OcultarAdmin):
    pass

admin.site.register(TipoOvinoCaprino,AdminTipoOvinoCaprino)
admin.site.register(OvinoCaprino)
admin.site.register(TipoProdutoOvinoCaprino,AdminTipoProdutoOvinoCaprino)
admin.site.register(ProdutoOvinoCaprino)

#Aves
class AdminTipoAve(OcultarAdmin):
    pass

class AdminTipoProdutoAve(OcultarAdmin):
    pass

admin.site.register(TipoAve,AdminTipoAve)
admin.site.register(Ave)
admin.site.register(TipoProdutoAve,AdminTipoProdutoAve)
admin.site.register(ProdutoAve)

#Apicultura
class AdminTipoProdutoApicultura(OcultarAdmin):
    pass

admin.site.register(TipoProdutoApicultura,AdminTipoProdutoApicultura)
admin.site.register(Apicultura)
admin.site.register(ProdutoApicultura)

#Psicultura
class AdminTipoProdutoPsicultura(OcultarAdmin):
    pass

admin.site.register(TipoProdutoPsicultura,AdminTipoProdutoPsicultura)
admin.site.register(Psicultura)
admin.site.register(ProdutoPsicultura)

#Outros ???
#admin.site.register(Outros)

#Culturas
class AdminTipoCultura(OcultarAdmin):
    pass

admin.site.register(TipoCultura,AdminTipoCultura)
admin.site.register(Cultura)

#Renda de Fora da Propriedade
admin.site.register(RendaForaPropriedade)

#Renda de Fora da Agricultura
admin.site.register(RendaForaAgricultura)

#Comercialização
class AdminTipoComercializacao(OcultarAdmin):
    pass

admin.site.register(TipoComercializacao,AdminTipoComercializacao)
admin.site.register(Comercializacao)

#Acesso a Políticas Públicas
class AdminPoliticaPublica(OcultarAdmin):
    pass

admin.site.register(PoliticaPublica,AdminPoliticaPublica)
admin.site.register(PoliticaPublica_UnidadeProducao)

#Organização Social
class AdminOrganizacaoSocial(OcultarAdmin):
    pass

admin.site.register(OrganizacaoSocial,AdminOrganizacaoSocial)
admin.site.register(OrganizacaoSocial_UnidadeProducao)