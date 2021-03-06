import uuid

from django import forms

from ajax_upload.models import UploadedFile
from ajax_upload.settings import FILE_FIELD_MAX_SIZE_MB

class UploadedFileForm(forms.ModelForm):

    class Meta:
        model = UploadedFile
        fields = ('file',)

    def clean_file(self):
        data = self.cleaned_data['file']
        # Change the name of the file to something unguessable
        # Construct the new name as <unique-hex>-<original>.<ext>
        data.name = u'%s-%s' % (uuid.uuid4().hex, data.name)
        if data.size * 9.53674e-7 > FILE_FIELD_MAX_SIZE_MB and FILE_FIELD_MAX_SIZE_MB != 0:
	        raise forms.ValidationError('The image is too big! (Maximum size allowed: ' + str(FILE_FIELD_MAX_SIZE_MB) + 'MB)')
        return data
