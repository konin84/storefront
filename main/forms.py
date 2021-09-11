from django import forms
from django.forms import DateInput
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['slug']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields = '__all__'


class AboutCompanyForm(forms.ModelForm):
    class Meta:
        model = About_us
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'


class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = '__all__'


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        widgets = {
            'Date_joined': DateInput(attrs={'type': 'date'}),
        }

'''
class TestForm(forms.ModelForm):
    class Meta:
        model = Testing
        fields = '__all__'

'''