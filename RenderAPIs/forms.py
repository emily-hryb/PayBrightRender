from django import forms

class InputForm(forms.Form):
     api_key = forms.CharField(label='The Sandbox API Key:', max_length=100)
     api_token = forms.CharField(label='The Sandbox API Token:', max_length=100)
     