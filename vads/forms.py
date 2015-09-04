from django import forms
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Button, Fieldset,\
    ButtonHolder
from vads.models import UserProfile
from crispy_forms.templatetags.crispy_forms_field import css_class

# Create your models here.

class UserProfileForm1(forms.Form):
    first_name = forms.CharField(label='First Name', required = True)
    last_name = forms.CharField(label='Last Name', required = True)
    middle_name = forms.CharField(label='Middle Name', required = False)
    # TODO: use the right file for phone
    phone = forms.CharField(label='Phone', required = False)
    address = forms.CharField(label='Address', required = False)
    city = forms.CharField(label='City', required = False)
    zipcode = forms.CharField(label='Zip Code', required = False)

    helper = FormHelper()
    helper.form_method = "POST"
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
    
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout('first_name',
                                    'last_name', 
                                    'user_type',
                                    ButtonHolder(Submit('update', 'Update', css_class='btn_primary')))
    
class ScreenForm(forms.ModelForm):
    class Meta:
        fields = ('name',)
        model = models.Screen
    
    def __init__(self, *args, **kwargs):
        super(ScreenForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                                    'name',
                                    ButtonHolder(Submit('create', 'Create', css_class='btn_primary')))
        
class AdForm(forms.ModelForm):
    class Meta:
        model = models.Ad
        fields = ('name','ad_type','info')
    
    def __init__(self, *args, **kwargs):
        super(AdForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                                    'name',
                                    'ad_type',
                                    'info',
                                    ButtonHolder(Submit('create', 'Create', css_class='btn_primary')))
    

class AdListForm(forms.ModelForm):
    class Meta:
        model = models.AdList
        fields = ('name', 'info')
    
    def __init__(self, *args, **kwargs):
        super(AdListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                                    'name',
                                    'info',
                                    ButtonHolder(Submit('create', 'Create', css_class='btn_primary')))
    