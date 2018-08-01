from django import forms


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(label='First Name', strip=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    last_name = forms.CharField(label='Last Name', strip=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    email = forms.EmailField(label='Email', required=False, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    username = forms.CharField(label='Username', strip=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))
    password_conf = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Retype your password'}))
