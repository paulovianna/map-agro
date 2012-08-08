# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.gis.gdal import SpatialReference,CoordTransform
from django.contrib.gis import gdal
from django.template import RequestContext
from forms import UploadForm
from models import *


def Inicio(request):
    
    return render_to_response('inicio.html',RequestContext(request,{}))

def Paises(request):
    
    tipo = 'Países'
    dados = Pais.objects.all()
    
    return render_to_response('lista.html',
                              RequestContext(request,{'dados':dados,
                                                      'tipo': tipo}))

def Mapa_Pais(request,id_pais):
    
    obj = Pais.objects.filter(id = id_pais)
    ct = CoordTransform(SpatialReference('EPSG:4326'), SpatialReference('EPSG:900913'))
    
    nome = ''
    for feat in obj:
        nome = feat.get_name()
        
    dados = []    
    for p in obj:
        aux = p.mpoly
        aux.transform(ct)
        dados.append(aux)
    
    return render_to_response('mapa.html',
                              RequestContext(request,{'dados':dados,
                                                      'nome':nome}))

def Regioes(request):
    
    tipo = 'Regiões'
    dados = Regiao.objects.all().order_by('regiao')
    
    return render_to_response('lista.html',
                              RequestContext(request,{'dados':dados,
                                                      'tipo': tipo}))

def Mapa_Regiao(request,id_regiao):
    
    obj = Regiao.objects.filter(id = id_regiao)
    ct = CoordTransform(SpatialReference('EPSG:4326'), SpatialReference('EPSG:900913'))
    
    nome = ''
    for feat in obj:
        nome = feat.get_name()
        
    dados = []    
    for p in obj:
        aux = p.mpoly
        aux.transform(ct)
        dados.append(aux)
    
    return render_to_response('mapa.html',
                              RequestContext(request,{'dados':dados,
                                                      'nome':nome})) 
    
def Estados(request):
    
    tipo = 'Estados'
    dados = Uf.objects.all().order_by('uf')
    
    return render_to_response('lista.html',
                              RequestContext(request,{'dados':dados,
                                                      'tipo': tipo}))

def Mapa_Estado(request,id_estado):
    
    obj = Uf.objects.filter(id = id_estado)
    ct = CoordTransform(SpatialReference('EPSG:4326'), SpatialReference('EPSG:900913'))
    
    nome = ''
    for feat in obj:
        nome = feat.get_name()
        
    dados = []    
    for p in obj:
        aux = p.mpoly
        aux.transform(ct)
        dados.append(aux)
    
    return render_to_response('mapa.html',
                              RequestContext(request,{'dados':dados,
                                                      'nome':nome})) 

def Mesorregioes(request):
    
    tipo = 'Mesorregiões'
    dados = MesoRegiao.objects.all().order_by('mesoRegiao')
    
    return render_to_response('lista.html',
                              RequestContext(request,{'dados':dados,
                                                      'tipo': tipo}))

def Mapa_Meso(request,id_meso):
    
    obj = MesoRegiao.objects.filter(id = id_meso)
    ct = CoordTransform(SpatialReference('EPSG:4326'), SpatialReference('EPSG:900913'))
    
    nome = ''
    for feat in obj:
        nome = feat.get_name()
        
    dados = []    
    for p in obj:
        aux = p.mpoly
        aux.transform(ct)
        dados.append(aux)
    
    return render_to_response('mapa.html',
                              RequestContext(request,{'dados':dados,
                                                      'nome':nome})) 
    
def Microrregioes(request):
    
    tipo = 'Microrregiões'
    dados = MicroRegiao.objects.all().order_by('microRegiao')
    
    return render_to_response('lista.html',
                              RequestContext(request,{'dados':dados,
                                                      'tipo': tipo}))

def Mapa_Micro(request,id_micro):
    
    obj = MicroRegiao.objects.filter(id = id_micro)
    ct = CoordTransform(SpatialReference('EPSG:4326'), SpatialReference('EPSG:900913'))
    
    nome = ''
    for feat in obj:
        nome = feat.get_name()
        
    dados = []    
    for p in obj:
        aux = p.mpoly
        aux.transform(ct)
        dados.append(aux)
    
    return render_to_response('mapa.html',
                              RequestContext(request,{'dados':dados,
                                                      'nome':nome})) 
    
def Municipios(request):
    
    tipo = 'Municípios'
    dados = Municipio.objects.all().order_by('municipio')
    
    return render_to_response('lista.html',
                              RequestContext(request,{'dados':dados,
                                                      'tipo': tipo}))

def Mapa_Municipio(request,id_municipio):
    
    obj = Municipio.objects.filter(id = id_municipio)
    ct = CoordTransform(SpatialReference('EPSG:4326'), SpatialReference('EPSG:900913'))
    
    nome = ''
    for feat in obj:
        nome = feat.get_name()
        
    dados = []    
    for p in obj:
        aux = p.mpoly
        aux.transform(ct)
        dados.append(aux)
    
    return render_to_response('mapa.html',
                              RequestContext(request,{'dados':dados,
                                                      'nome':nome})) 

def upload(request):
    ctoken = {}
    ctoken.update(csrf(request))
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            shp = form.handle(request.FILES['file_obj'])
            ds = gdal.DataSource(shp)
            ct = CoordTransform(SpatialReference('EPSG:4326'), SpatialReference('EPSG:900913'))
            
            dados=[]
            for layer in ds[0]:
                aux = layer.geom
                aux.transform(ct)
                dados.append(aux)
            
            form = UploadForm()
            return render_to_response('googlev3_upload.html', 
                                      RequestContext(request,{'form': form,
                                                              'dados': dados, 'token':ctoken}))
    else:
        form = UploadForm()
    return render_to_response('googlev3_upload.html', 
                              RequestContext(request,{'form': form}))
    

def RegioesGeopoliticas(request):
    
    regioes = RegiaoGeoPolitica.objects.all()
    
    return render_to_response('regioes_geopoliticas.html', 
                              RequestContext(request,{'regioes': regioes}))
    

def RegiaoGeopolitica(request,id_geopolitica):
    
    regiao = RegiaoGeoPolitica.objects.filter(id = id_geopolitica)
    ct = CoordTransform(SpatialReference('EPSG:4326'), SpatialReference('EPSG:900913'))
    
    nome = ''
    for feat in regiao:
        regiaogeo = feat.municipios.all()
        nome = feat.regiaoGeoPolitica
        
    dados = []    
    for r in regiaogeo:
        aux = r.mpoly
        aux.transform(ct)
        dados.append(aux)
    
    return render_to_response('regiao_geopolitica.html', 
                              RequestContext(request,{'regiao': regiaogeo,
                                                      'dados' : dados,
                                                      'nome' : nome}))
    