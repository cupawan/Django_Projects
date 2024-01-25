from django import forms

class TranslateForm(forms.Form):
    api_key = forms.CharField(label='API KEY', max_length=100,widget=forms.PasswordInput)
    text = forms.CharField(label='Text', max_length=200)
    target_language = forms.CharField(label='Translate To', max_length=200)