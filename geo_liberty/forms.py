import os
import zipfile
import tempfile
from django import forms
from django.forms.util import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class UploadForm(forms.Form):

    file_obj  = forms.FileField(label=_('Upload a Zipped Shapefile'))
    
    def clean_file_obj(self):
        f = self.cleaned_data['file_obj']
        valid_shp, error = self.validate(f)
        if not valid_shp:
            raise ValidationError("A problem occured: %s" % error)

    def handle(self,filefield_data):
        
        upload_dir = settings.SHP_UPLOAD_DIR + filefield_data.name
        
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir) 
        
        downloaded_file = os.path.normpath(os.path.join(upload_dir, filefield_data.name)) 
        
        self.write_file(downloaded_file,filefield_data)
        
        zfobj = zipfile.ZipFile(downloaded_file)
        shp = os.path.splitext(zfobj.namelist()[0])[0]
        zfobj.extractall(upload_dir)
        
        shp_path = upload_dir + '/' + shp + '.shp'
        
        return shp_path

    def write_file(self,filename,filefield_data):
        destination = open(filename, 'wb+')
        for chunk in filefield_data.chunks():
            destination.write(chunk)
        destination.close()        

    def check_zip_contents(self, ext, zip_file):
        if not True in [info.filename.endswith(ext) for info in zip_file.infolist()]:
            return False
        return True

    def validate(self,filefield_data):
        
        tmp = tempfile.NamedTemporaryFile(suffix='.zip', mode = 'w')
        
        
        self.write_file(tmp.name,filefield_data)

        if not zipfile.is_zipfile(tmp.name):
            return False, 'That file is not a valid Zip Archive'

        zfile = zipfile.ZipFile(tmp.name)
        
        if not self.check_zip_contents('shp', zfile):
            return False, 'Found Zip Archive but no file with a .shp extension found inside.'
        #elif not self.check_zip_contents('prj', zfile):
            #return False, 'You must supply a .prj file with the Shapefile to indicate the projection.'
        elif not self.check_zip_contents('dbf', zfile):
            return False, 'You must supply a .dbf file with the Shapefile to supply attribute data.'
        elif not self.check_zip_contents('shx', zfile):
            return False, 'You must supply a .shx file for the Shapefile to have a valid index.'
        
        return True, None