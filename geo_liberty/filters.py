# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
from models import MicroRegiao, MesoRegiao

class mesoRegiaoFilter(SimpleListFilter):
    title = _(u'Mesorregião')
    parameter_name = 'meso'

    def lookups(self, request, model_admin):
        var = []
        parametro = None;
        if request.GET:
            try:
                if "microRegiao__mesoRegiao__uf__id__exact" in request.GET:
                    parametro = request.GET["microRegiao__mesoRegiao__uf__id__exact"]
                elif "mesoRegiao__uf__id__exact" in request.GET:
                    parametro = request.GET["mesoRegiao__uf__id__exact"]
                    
                if parametro:
                    objetos = MesoRegiao.objects.all().filter(uf=parametro)
                    for o in objetos:
                        var.append((str(o.id), _(o.mesoRegiao)))
                        
            except KeyError:
                pass
        
        return var

    def queryset(self, request, queryset):
        if self.value():
            if "microRegiao__mesoRegiao__uf__id__exact" in request.GET:
                return queryset.filter(microRegiao__mesoRegiao=self.value())
            elif "mesoRegiao__uf__id__exact" in request.GET:
                return queryset.filter(mesoRegiao=self.value())
            
        
class microRegiaoFilter(SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _(u'Microrregião')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'micro'

    def lookups(self, request, model_admin):
        var = []
        if request.GET:
            try:
                parametro = request.GET["meso"]
                if parametro:
                    objetos = MicroRegiao.objects.all().filter(mesoRegiao=parametro)
                    for o in objetos:
                        var.append((str(o.id), _(o.microRegiao)))
            except KeyError:
                pass
        
        return var

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(microRegiao=self.value())