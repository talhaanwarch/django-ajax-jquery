from django.shortcuts import render
from .form import TextForm
from django.http import JsonResponse
from .models import TextModel
# Create your views here.
from django.shortcuts import render
from django.forms.models import model_to_dict

def home(request):
	if request.method=='POST':
		form = TextForm(request.POST)
		if form.is_valid():
			out=form.save()
			#cleaned_data is built in function but before that is_valid must be called
			output=form.cleaned_data['text']
			print(output)
			return JsonResponse({'text':model_to_dict(out)},status=200)
	else:
		form = TextForm()
		return render(request,'home.html',{'form':form})

