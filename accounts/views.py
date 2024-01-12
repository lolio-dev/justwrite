from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from .forms import SignUpForm


# Create your views here.
@require_POST
def signup(request):
	form = SignUpForm(request.POST)

	if form.is_valid():
		print(form.cleaned_data)

	return redirect('index')
