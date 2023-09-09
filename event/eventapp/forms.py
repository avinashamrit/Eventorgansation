from django import forms
from .models import Family

class Familyforms(forms.ModelForm):
    class Meta:
        Model=Family
        fields='__all__'