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

class PoliticaPublicaInline(admin.StackedInline):
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
class FamiliaInline(admin.StackedInline):
    model = Familia
    extra = 0

class AdminBeneficiario(admin.ModelAdmin):
    fieldsets = (
            (None, {
                'fields': (('uf','mesoRegiao'),('microRegiao','municipio'),'denominacao',('rg','sexo'),('cpf','dataNascimento','estadoCivil'),
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

class AdminTipoProdutoBovinocultura(OcultarAdmin):
    pass

class BovinoInline(admin.StackedInline):
    model = Bovino
    extra = 0
    
class ProdutoBovinoculturaInline(admin.TabularInline):
    model = ProdutoBovinocultura
    extra = 1
    
class AdminBovinocultura(admin.ModelAdmin):
    inlines = [ProdutoBovinoculturaInline,]
    
admin.site.register(TipoBovino,AdminTipoBovino)
admin.site.register(TipoProdutoBovinocultura,AdminTipoProdutoBovinocultura)
admin.site.register(Bovinocultura,AdminBovinocultura)

#Suino
class AdminTipoSuino(OcultarAdmin):
    pass

class AdminTipoProdutoSuinocultura(OcultarAdmin):
    pass

class SuinoInline(admin.StackedInline):
    model = Suino
    extra = 0
    
class ProdutoSuinoculturaInline(admin.TabularInline):
    model = ProdutoSuinocultura
    extra = 1
    
class AdminSuinocultura(admin.ModelAdmin):
    inlines = [ProdutoSuinoculturaInline,]

admin.site.register(TipoSuino,AdminTipoSuino)
admin.site.register(TipoProdutoSuinocultura,AdminTipoProdutoSuinocultura)
admin.site.register(Suinocultura,AdminSuinocultura)

#Ovino/Caprino
class AdminTipoOvinoCaprino(OcultarAdmin):
    pass

class AdminTipoProdutoOvinocaprinocultura(OcultarAdmin):
    pass

class OvinoCaprinoInline(admin.StackedInline):
    model = OvinoCaprino
    extra = 0
    
class ProdutoOvinocaprinoculturaInline(admin.TabularInline):
    model = ProdutoOvinocaprinocultura
    extra = 1
    
class AdminOvinocaprinocultura(admin.ModelAdmin):
    inlines = [ProdutoOvinocaprinoculturaInline,]

admin.site.register(TipoOvinoCaprino,AdminTipoOvinoCaprino)
admin.site.register(TipoProdutoOvinocaprinocultura,AdminTipoProdutoOvinocaprinocultura)
admin.site.register(Ovinocaprinocultura,AdminOvinocaprinocultura)

#Aves
class AdminTipoAve(OcultarAdmin):
    pass

class AdminTipoProdutoAvicultura(OcultarAdmin):
    pass

class AveInline(admin.StackedInline):
    model = Ave
    extra = 0
    
class ProdutoAviculturaInline(admin.TabularInline):
    model = ProdutoAvicultura
    extra = 1
    
class AdminAvicultura(admin.ModelAdmin):
    inlines = [ProdutoAviculturaInline,]

admin.site.register(TipoAve,AdminTipoAve)
admin.site.register(TipoProdutoAvicultura,AdminTipoProdutoAvicultura)
admin.site.register(Avicultura,AdminAvicultura)

#Apicultura
class AdminTipoProdutoApicultura(OcultarAdmin):
    pass

class AbelhaInline(admin.StackedInline):
    model = Apicultura
    extra = 0
    
class ProdutoApiculturaInline(admin.TabularInline):
    model = ProdutoApicultura
    extra = 1
    
class AdminApicultura(admin.ModelAdmin):
    inlines = [ProdutoApiculturaInline,]

admin.site.register(TipoProdutoApicultura,AdminTipoProdutoApicultura)
admin.site.register(Apicultura,AdminApicultura)

#Psicultura
class AdminTipoProdutoPsicultura(OcultarAdmin):
    pass

class PeixeInline(admin.StackedInline):
    model = Peixe
    extra = 0
    
class ProdutoPsciculturaInline(admin.TabularInline):
    model = ProdutoPscicultura
    extra = 1
    
class AdminPscicultura(admin.ModelAdmin):
    inlines = [ProdutoPsciculturaInline,]

admin.site.register(TipoProdutoPscicultura,AdminTipoProdutoPsicultura)
admin.site.register(Pscicultura,AdminPscicultura)

#Outros ???
#admin.site.register(Outros)

#Culturas Agrícolas
class AdminTipoCultura(OcultarAdmin):
    pass

class ProdutoAgricolaInline(admin.TabularInline):
    model = ProdutoAgricola
    extra = 1
    
class AdminAgricultura(admin.ModelAdmin):
    inlines = [ProdutoAgricolaInline,]

admin.site.register(TipoCultura,AdminTipoCultura)
admin.site.register(Agricultura,AdminAgricultura)

#Extrativismo
class AdminTipoExtrativismo(OcultarAdmin):
    pass

class ProdutoExtrativismoInline(admin.TabularInline):
    model = ProdutoExtrativismo
    extra = 1

class AdminExtrativismo(admin.ModelAdmin):
    inlines = [ProdutoExtrativismoInline,]

admin.site.register(TipoExtrativismo,AdminTipoExtrativismo)
admin.site.register(Extrativismo,AdminExtrativismo)

#Unidade de Produção
class AdminTerra(OcultarAdmin):
    pass

class TerraInline(admin.TabularInline):
    model = Terra_UnidadeProducao
    extra = 0

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
    
class ConfrontacaoInline(admin.StackedInline):
    model = Confrontacao
    extra = 0

class AdminUnidadeProducao(AdminGeo):
    filter_horizontal = ('destinoLixo','utilizacaoAgrotoxico','destinoEmbalagemAgrotoxico',
                        'preparoSolo','praticaConservacaoSolo','insumosOrganicos','utilizacaoArvores',)
    fieldsets = (
            (None, {
                'fields': (('uf','mesoRegiao'),('microRegiao','municipio','beneficiario'),'ponto','denominacao',('localizacao','area'),
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
               TerraInline,
               BenfeitoriaInline,
               EquipamentoTrabalhoInline,
               BovinoInline,
               SuinoInline,
               OvinoCaprinoInline,
               AveInline,
               AbelhaInline,
               PeixeInline,
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