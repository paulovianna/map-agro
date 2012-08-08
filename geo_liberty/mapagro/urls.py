from django.conf.urls.defaults import patterns,url

from views import *

urlpatterns = patterns('mapagro',
     
     url(r'^$', Inicio),
     url(r'^mapa_beneficiarios/$', MapaBeneficiarios),
     url(r'^beneficiarios/$', Beneficiarios),
     url(r'^login/$', Login),
     url(r'^logout/$', Logout),
     url(r'^unidade/(?P<id_unidade>\d+)/$', AbrirUnidadeProducao),
     url(r'^beneficiario/(?P<id_beneficiario>\d+)/$', AbrirBeneficiario),
     url(r'^renda/(?P<id_unidade>\d+)/(?P<id_beneficiario>\d+)/$', AbrirRenda),
)