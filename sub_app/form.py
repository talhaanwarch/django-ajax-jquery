from django import forms
from .models import TextModel

class TextForm(forms.ModelForm):
	class Meta:
		model=TextModel
		fields = "__all__"
		widgets={
		'text':forms.TextInput(attrs={'class':'form-control','id':'textid'})

		}