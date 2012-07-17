from django.conf.urls.defaults import patterns,url

from views import MapaUnidadeProducao,AbrirUnidadeProducao,AbrirBeneficiario,AbrirRenda

urlpatterns = patterns('mapagro',
     
     url(r'^$', MapaUnidadeProducao),
     url(r'^unidade/(?P<id_unidade>\d+)/$', AbrirUnidadeProducao),
     url(r'^beneficiario/(?P<id_beneficiario>\d+)/$', AbrirBeneficiario),
     url(r'^renda/(?P<id_unidade>\d+)/(?P<id_beneficiario>\d+)/$', AbrirRenda),
)