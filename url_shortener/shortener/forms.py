from django import forms

class URLForm(forms.Form):
    original_url = forms.URLField(label='URL to shorten', max_length=200)
