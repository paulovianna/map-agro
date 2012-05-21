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
    
#Acesso a Políticas Públicas
class AdminPoliticaPublica(OcultarAdmin):
    pass

class PoliticaPublicaInline(admin.TabularInline):
    model = PoliticaPublica_Beneficiario
    extra = 0

admin.site.register(PoliticaPublica,AdminPoliticaPublica)

#Organização Social
class AdminOrganizacaoSocial(OcultarAdmin):
    pass

class OrganizacaoSocialInline(admin.TabularInline):
    model = OrganizacaoSocial_Beneficiario
    extra = 0
    
admin.site.register(OrganizacaoSocial,AdminOrganizacaoSocial)

#Rendas
class RendaForaPropriedadeInline(admin.TabularInline):
    model = RendaForaPropriedade
    extra = 0
    
class RendaForaAgriculturaInline(admin.TabularInline):
    model = RendaForaAgricultura
    extra = 0
       
#Beneficiario 
class FamiliaInline(admin.TabularInline):
    model = Familia
    extra = 0

class AdminBeneficiario(admin.ModelAdmin):
    fieldsets = (
            (None, {
                'fields': ('municipio','denominacao',('rg','sexo'),('cpf','dataNascimento','estadoCivil'),
                           ('endereco','telefone'),('dap','situacao','classificacao'),)
            }),
        )
    inlines  = [FamiliaInline,
                PoliticaPublicaInline,
                OrganizacaoSocialInline,
                RendaForaPropriedadeInline,
                RendaForaAgriculturaInline,]
   
admin.site.register(Beneficiario,AdminBeneficiario)

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

#Bovinos
class AdminTipoBovino(OcultarAdmin):
    pass

class AdminTipoProdutoBovino(OcultarAdmin):
    pass

class BovinoInline(admin.TabularInline):
    model = Bovino
    extra = 0
    
admin.site.register(TipoBovino,AdminTipoBovino)
admin.site.register(TipoProdutoBovino,AdminTipoProdutoBovino)
admin.site.register(ProdutoBovino)

#Suino
class AdminTipoSuino(OcultarAdmin):
    pass

class AdminTipoProdutoSuino(OcultarAdmin):
    pass

class SuinoInline(admin.TabularInline):
    model = Suino
    extra = 0

admin.site.register(TipoSuino,AdminTipoSuino)
admin.site.register(TipoProdutoSuino,AdminTipoProdutoSuino)
admin.site.register(ProdutoSuino)

#Ovino/Caprino
class AdminTipoOvinoCaprino(OcultarAdmin):
    pass

class AdminTipoProdutoOvinoCaprino(OcultarAdmin):
    pass

class OvinoCaprinoInline(admin.TabularInline):
    model = OvinoCaprino
    extra = 0

admin.site.register(TipoOvinoCaprino,AdminTipoOvinoCaprino)
admin.site.register(TipoProdutoOvinoCaprino,AdminTipoProdutoOvinoCaprino)
admin.site.register(ProdutoOvinoCaprino)

#Aves
class AdminTipoAve(OcultarAdmin):
    pass

class AdminTipoProdutoAve(OcultarAdmin):
    pass

class AveInline(admin.TabularInline):
    model = Ave
    extra = 0

admin.site.register(TipoAve,AdminTipoAve)
admin.site.register(TipoProdutoAve,AdminTipoProdutoAve)
admin.site.register(ProdutoAve)

#Apicultura
class AdminTipoProdutoApicultura(OcultarAdmin):
    pass

class ApiculturaInline(admin.TabularInline):
    model = Apicultura
    extra = 1

admin.site.register(TipoProdutoApicultura,AdminTipoProdutoApicultura)
admin.site.register(ProdutoApicultura)

#Psicultura
class AdminTipoProdutoPsicultura(OcultarAdmin):
    pass

class PsiculturaInline(admin.TabularInline):
    model = Psicultura
    extra = 0

admin.site.register(TipoProdutoPsicultura,AdminTipoProdutoPsicultura)
admin.site.register(ProdutoPsicultura)

#Outros ???
#admin.site.register(Outros)

#Culturas
class AdminTipoCultura(OcultarAdmin):
    pass

admin.site.register(TipoCultura,AdminTipoCultura)
admin.site.register(Cultura)

#Unidade de Produção
class AdminTerra(OcultarAdmin):
    pass

class AdminBenfeitoria(OcultarAdmin):
    pass

class BenfeitoriaInline(admin.TabularInline):
    model = Benfeitoria_UnidadeProducao
    extra = 0

class AdminEquipamentoTrabalho(OcultarAdmin):
    pass

class EquipamentoTrabalhoInline(admin.TabularInline):
    model = EquipamentoTrabalho_UnidadeProducao
    extra = 0
    
class ConfrontacaoInline(admin.TabularInline):
    model = Confrontacao
    extra = 0

class AdminUnidadeProducao(AdminGeo):
    filter_horizontal = ('destinoLixo','utilizacaoAgrotoxico','destinoEmbalagemAgrotoxico',
                        'preparoSolo','praticaConservacaoSolo','insumosOrganicos','utilizacaoArvores',)
    fieldsets = (
            (None, {
                'fields': ('municipio','ponto',('denominacao','beneficiario'),('localizacao','area'),
                           ('tituloDominio','participacao'),('registro','dataRegistro'),'receitaFederal')
            }),
            ('Avançado', {
                'classes': ('collapse',),
                'fields': ('qualidadeAgua','destinoLixo','utilizacaoAgrotoxico','destinoEmbalagemAgrotoxico',
                           'preparoSolo','areaErosao','praticaConservacaoSolo','insumosOrganicos','rotacaoCultura',
                           'utilizacaoArvores')
            }),
        )
    inlines = [ConfrontacaoInline,
               BenfeitoriaInline,
               EquipamentoTrabalhoInline,
               BovinoInline,
               SuinoInline,
               OvinoCaprinoInline,
               AveInline,
               ApiculturaInline,
               PsiculturaInline,
               ]

admin.site.register(UnidadeProducao,AdminUnidadeProducao)
admin.site.register(Terra,AdminTerra)
admin.site.register(Benfeitoria,AdminBenfeitoria)
admin.site.register(EquipamentoTrabalho,AdminEquipamentoTrabalho)

#Comercialização
class AdminTipoComercializacao(OcultarAdmin):
    pass

admin.site.register(TipoComercializacao,AdminTipoComercializacao)
admin.site.register(Comercializacao)