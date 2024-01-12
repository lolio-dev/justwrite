from django.shortcuts import render

from accounts.forms import SignUpForm


# Create your views here.
def home_page(request):
	signup_form = SignUpForm()

	return render(request, 'index.html', {
		'signup_form': signup_form
	})
