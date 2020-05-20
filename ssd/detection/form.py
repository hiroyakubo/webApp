from django import forms

from .models import Image

class ImageForms(forms.ModelForm):
    class Meta:
        model = Image
        fields = (
            "title", 
            "picture", 
        )