from django import forms
from .models import CompressImage

class ImageForm(forms.ModelForm):
    class Meta:
        model = CompressImage
        fields= ['image',]
