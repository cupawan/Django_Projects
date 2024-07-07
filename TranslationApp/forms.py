from django import forms

class TranslateForm(forms.Form):
    text = forms.CharField(label='Text', max_length=200)
    target_language = forms.CharField(label='Translate To', max_length=200)
