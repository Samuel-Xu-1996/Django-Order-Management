'''
from django.forms import ModelForm
from django import forms
from .models import BillAddress, ShipAddress


billAddress_id = forms.ModelChoiceField(queryset=BillAddress.objects.filter(active='1'), empty_label='')
shipAddress_id = forms.ModelChoiceField(queryset=ShipAddress.objects.filter(active='1'), empty_label='')

class BillAddressForm(ModelForm):
    class Meta:
        model = BillAddress
        fields = ['bill_address']

class ShipAddressForm(ModelForm):
    class Meta:
        model = ShipAddress
        fields = ['ship_address']
        '''
