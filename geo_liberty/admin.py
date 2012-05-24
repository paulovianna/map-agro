from django.contrib.gis import admin
from models import *
from filters import *

class AdminGeo(admin.OSMGeoAdmin):
    
    scrollable = True
    map_width = 700
    map_height = 350
    
class PaisAdmin(AdminGeo):
    list_display = ['pais','sigla',]
    search_fields = ['pais', 'sigla']
    
class RegiaoAdmin(AdminGeo):
    list_display = ['regiao', 'pais']
    list_filter = ['pais']
    search_fields = ['regiao', 'pais__pais']

class UfAdmin(AdminGeo):
    list_display = ['uf', 'regiao',]
    list_filter = ['regiao',]
    search_fields = ['uf', 'regiao__regiao','regiao__pais__pais']

class MesoRegiaoAdmin(AdminGeo):
    list_display = ['mesoRegiao', 'uf']
    list_filter = ['uf',]
    search_fields = ['mesoRegiao', 'uf__uf']

class MicroRegiaoAdmin(AdminGeo):
    list_display = ['microRegiao', 'mesoRegiao']
    list_filter = ['mesoRegiao__uf', mesoRegiaoFilter]
    search_filds = ['microRegiao', 'mesoRegiao__mesoRegiao', 'mesoRegiao__uf__uf']

class MunicipioAdmin(AdminGeo):
    search_fields = ['municipio']
    list_display = ['municipio','microRegiao',]
    list_filter = ['microRegiao__mesoRegiao__uf',mesoRegiaoFilter,microRegiaoFilter]
    
    
admin.site.register(Pais,PaisAdmin)
admin.site.register(Regiao,RegiaoAdmin)
admin.site.register(Uf,UfAdmin)
admin.site.register(MesoRegiao,MesoRegiaoAdmin)
admin.site.register(MicroRegiao,MicroRegiaoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(RegiaoGeoPolitica,AdminGeo)