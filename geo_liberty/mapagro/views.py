from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.gis.gdal import SpatialReference,CoordTransform

from models import UnidadeProducao

def MapaUnidadeProducao(request):
    
    from geo_liberty.models import Municipio
    
    unidades = UnidadeProducao.objects.all()
    taquarucu = Municipio.objects.filter(id = 4321329)
    
    ct = CoordTransform(SpatialReference('EPSG:4326'), SpatialReference('EPSG:900913'))
    
    for feat in unidades:
        feat.ponto.transform(ct)
    
    for feat in taquarucu:
        municipio = feat.mpoly
        municipio.transform(ct)
    
    return render_to_response('frontend/mapa_unidades_producao.html', 
                              RequestContext(request,{'unidades': unidades,
                                                      'municipio':municipio}))
    

def AbrirUnidadeProducao(request,id_unidade):
    
    from models import Confrontacao,Terra_UnidadeProducao,Benfeitoria_UnidadeProducao,EquipamentoTrabalho_UnidadeProducao,Bovino,Suino,OvinoCaprino,Ave,Abelha,Peixe
    
    unidade = UnidadeProducao.objects.filter(id=id_unidade)
    confrontacao = Confrontacao.objects.filter(unidadeProducao=id_unidade)
    terras = Terra_UnidadeProducao.objects.filter(unidadeProducao=id_unidade)
    benfeitorias = Benfeitoria_UnidadeProducao.objects.filter(unidadeProducao=id_unidade)
    equipamentos = EquipamentoTrabalho_UnidadeProducao.objects.filter(unidadeProducao=id_unidade)
    bovinos = Bovino.objects.filter(unidadeProducao=id_unidade)
    suinos = Suino.objects.filter(unidadeProducao=id_unidade)
    ovinos = OvinoCaprino.objects.filter(unidadeProducao=id_unidade)
    aves = Ave.objects.filter(unidadeProducao=id_unidade)
    abelhas = Abelha.objects.filter(unidadeProducao=id_unidade)
    peixes = Peixe.objects.filter(unidadeProducao=id_unidade)
    
    return render_to_response('frontend/unidade_producao.html', 
                              RequestContext(request,{'unidade':unidade,
                                                      'confrontacao':confrontacao,
                                                      'terras':terras,
                                                      'benfeitorias':benfeitorias,
                                                      'equipamentos':equipamentos,
                                                      'bovinos':bovinos,
                                                      'suinos':suinos,
                                                      'ovinos':ovinos,
                                                      'aves':aves,
                                                      'abelhas':abelhas,
                                                      'peixes':peixes}))
    
    
def AbrirBeneficiario(request,id_beneficiario):
    
    from models import Beneficiario,Familia,PoliticaPublica_Beneficiario,OrganizacaoSocial_Beneficiario
    
    beneficiario = Beneficiario.objects.filter(id=id_beneficiario)
    familia = Familia.objects.filter(beneficiario=id_beneficiario)
    politicasPublicas = PoliticaPublica_Beneficiario.objects.filter(beneficiario=id_beneficiario)
    organizacoesSociais = OrganizacaoSocial_Beneficiario.objects.filter(beneficiario=id_beneficiario)


    return render_to_response('frontend/beneficiario.html', 
                              RequestContext(request,{'beneficiario': beneficiario,
                                                      'familia':familia,
                                                      'politicasPublicas':politicasPublicas,
                                                      'organizacoesSociais':organizacoesSociais}))
    
    
def AbrirRenda(request,id_unidade,id_beneficiario):
    
    from models import Agricultura,ProdutoAgricola,Extrativismo,ProdutoExtrativismo
    from models import Bovinocultura,ProdutoBovinocultura,Suinocultura,ProdutoSuinocultura
    from models import Ovinocaprinocultura,ProdutoOvinocaprinocultura,Avicultura,ProdutoAvicultura
    from models import Apicultura,ProdutoApicultura,Pscicultura,ProdutoPscicultura
    from models import RendaForaPropriedade,RendaForaAgricultura,Comercializacao,ProdutoComercializacao
    
    agricultura = Agricultura.objects.filter(unidadeProducao=id_unidade)
    if agricultura:
        for a in agricultura:
            produtosAgricolas = ProdutoAgricola.objects.filter(agricultura=a.id)
    else:
        produtosAgricolas = False
        
    extrativismo = Extrativismo.objects.filter(unidadeProducao=id_unidade)
    if extrativismo:
        for e in extrativismo:
            produtosExtrativistas = ProdutoExtrativismo.objects.filter(extrativismo=e.id)
    else:
        produtosExtrativistas = False
        
    bovinocultura = Bovinocultura.objects.filter(unidadeProducao=id_unidade)
    if bovinocultura:
        for b in bovinocultura:
            produtosBovinocultura = ProdutoBovinocultura.objects.filter(bovinocultura=b.id)
    else:
        produtosBovinocultura = False
        
    suinocultura = Suinocultura.objects.filter(unidadeProducao=id_unidade)
    if suinocultura:
        for s in suinocultura:
            produtosSuinocultura = ProdutoSuinocultura.objects.filter(suinocultura=s.id)
    else:
        produtosSuinocultura = False
        
    ovinocaprinocultura = Ovinocaprinocultura.objects.filter(unidadeProducao=id_unidade)
    if ovinocaprinocultura:
        for o in ovinocaprinocultura:
            produtosOvinocaprinocultura = ProdutoOvinocaprinocultura.objects.filter(ovinoaprinocultura=o.id)
    else:
        produtosOvinocaprinocultura = False
        
    avicultura = Avicultura.objects.filter(unidadeProducao=id_unidade)
    if avicultura:
        for av in avicultura:
            produtosAvicultura = ProdutoAvicultura.objects.filter(avicultura=av.id)
    else:
        produtosAvicultura = False
        
    apicultura = Apicultura.objects.filter(unidadeProducao=id_unidade)
    if apicultura:
        for ap in apicultura:
            produtosApicultura = ProdutoApicultura.objects.filter(apicultura=ap.id)
    else:
        produtosApicultura = False
        
    pscicultura = Pscicultura.objects.filter(unidadeProducao=id_unidade)
    if pscicultura:
        for ps in pscicultura:
            produtosPscicultura = ProdutoPscicultura.objects.filter(pscicultura=ps.id)
    else:
        produtosPscicultura = False
        
    comercializacao = Comercializacao.objects.filter(unidadeProducao=id_unidade)
    if comercializacao:
        for c in comercializacao:
            produtosComercializacao = ProdutoComercializacao.objects.filter(comercializacao=c.id)
    else:
        produtosComercializacao = False
        
    rendaForaPropriedade = RendaForaPropriedade.objects.filter(beneficiario=id_beneficiario)
    
    rendaForaAgricultura = RendaForaAgricultura.objects.filter(beneficiario=id_beneficiario)

    return render_to_response('frontend/renda.html', 
                              RequestContext(request,{'produtosAgricolas':produtosAgricolas,
                                                      'produtosExtrativistas':produtosExtrativistas,
                                                      'produtosBovinocultura':produtosBovinocultura,
                                                      'produtosSuinocultura':produtosSuinocultura,
                                                      'produtosOvinocaprinocultura':produtosOvinocaprinocultura,
                                                      'produtosAvicultura':produtosAvicultura,
                                                      'produtosApicultura':produtosApicultura,
                                                      'produtosPscicultura':produtosPscicultura,
                                                      'produtosComercializacao':produtosComercializacao,
                                                      'rendaForaPropriedade':rendaForaPropriedade,
                                                      'rendaForaAgricultura':rendaForaAgricultura}))




    