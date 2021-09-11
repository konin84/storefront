from django.forms import ModelForm, Textarea
from .models import *
from django import forms


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'rows': 4, 'cols': 20, 'style': 'resize:none;'}),
             }

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select category"
        self.fields['category'].required = True
