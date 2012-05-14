from django.contrib.gis import admin
from models import *

class AdminGeo(admin.OSMGeoAdmin):
    
    scrollable = True
    map_width = 700
    map_height = 350
    
admin.site.register(Pais,AdminGeo)
admin.site.register(Regiao,AdminGeo)
admin.site.register(Uf,AdminGeo)
admin.site.register(MesoRegiao,AdminGeo)
admin.site.register(MicroRegiao,AdminGeo)
admin.site.register(Municipio,AdminGeo)
admin.site.register(RegiaoGeoPolitica,AdminGeo)