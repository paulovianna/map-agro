# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.gis.gdal import SpatialReference,CoordTransform
from django.contrib.gis import gdal
from django.template import RequestContext
from forms import UploadForm

    
def upload(request):
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
                                                              'dados': dados}))
    else:
        form = UploadForm()
    return render_to_response('googlev3_upload.html', 
                              RequestContext(request,{'form': form}))