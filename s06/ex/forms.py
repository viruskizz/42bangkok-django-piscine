from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2'})
    )

    password = forms.CharField(
        label='Password',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2'})
    )