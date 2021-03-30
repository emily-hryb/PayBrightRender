from django import forms

class InputForm(forms.Form):
     api_key = forms.CharField(label='The Sandbox API Key:', max_length=100)
     api_token = forms.CharField(label='The Sandbox API Token:', max_length=100)
     amount = forms.DecimalField(label='The Amount:', decimal_places=2)
     currency = forms.CharField(label='The Currency:', max_length=100)     
     phone = forms.CharField(label='The Phone Number:',max_length=9) 
     
     