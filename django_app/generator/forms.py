from django import forms

class GeneratorForm(forms.Form):
    template_intro = forms.CharField(max_length=5000)
    template_chapitres = forms.CharField(max_length=5000)
    template_conclusion = forms.CharField(max_length=5000)
    mots_cles = forms.CharField(max_length=10000)