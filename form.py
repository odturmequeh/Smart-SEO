from django import forms

class Urlform(forms.Form):
    url=forms.CharField(max_length=100)
        