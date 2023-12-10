from django import forms
from hello.models import Invite

class InvitesForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ['nom', 'prenom', 'email', 'presence_confirme', 'preferences_alimentaires']
