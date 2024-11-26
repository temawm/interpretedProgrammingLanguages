from django import forms
from .models import Client, Policy, Claim

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']

class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['policynumber', 'client', 'policytype', 'startdate', 'enddate']

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['policy', 'claimdate', 'amount', 'status']