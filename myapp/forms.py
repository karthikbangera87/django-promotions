from django import forms
from .models import myapp

class EmailForm(forms.Form):
	''' Email form '''
	name = forms.CharField()
	email = forms.EmailField()


class myappmodelforms(forms.ModelForm):
	class Meta:
		model = myapp

		fields = ['email',]