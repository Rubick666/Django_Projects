from django import forms
from .models import Members

class MembersForm(forms.ModelForm):
    class meta:
        model = Members
        fields = "__all__"

