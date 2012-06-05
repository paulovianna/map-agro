# -*- coding: utf-8 -*- 
from django import forms
from models import UnidadeProducao

class FormUnidadeProducao(forms.ModelForm):
    
    longrau = forms.DecimalField(label='Lon Graus',widget=forms.TextInput(attrs={'size':'5'}),required=False)
    lonminuto = forms.DecimalField(label='Minutos',widget=forms.TextInput(attrs={'size':'5'}),required=False)
    lonsegundo = forms.DecimalField(label='Segundos',widget=forms.TextInput(attrs={'size':'5'}),required=False)
    latgrau = forms.DecimalField(label='Lat Graus',widget=forms.TextInput(attrs={'size':'5'}),required=False)
    latminuto = forms.DecimalField(label='Minutos',widget=forms.TextInput(attrs={'size':'5'}),required=False)
    latsegundo = forms.DecimalField(label='Segundos',widget=forms.TextInput(attrs={'size':'5'}),required=False)
    
    class Meta:
        fields = ('longrau','lonminuto','lonsegundo','latgrau','latminuto','latsegundo',
                  'municipio','beneficiario','ponto','denominacao','localizacao','area',
                  'tituloDominio','participacao','registro','dataRegistro',
                  'receitaFederal','qualidadeAgua','destinoLixo','utilizacaoAgrotoxico',
                  'destinoEmbalagemAgrotoxico','preparoSolo','areaErosao','praticaConservacaoSolo',
                  'insumosOrganicos','rotacaoCultura','utilizacaoArvores',)
        model = UnidadeProducao
        