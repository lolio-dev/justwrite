from django import forms


class SignUpForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput)
	username = forms.CharField(min_length=3, max_length=16)
	password = forms.CharField(widget=forms.PasswordInput, min_length=6)
	confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=6)
	cgu_accept = forms.BooleanField()
