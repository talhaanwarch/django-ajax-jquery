from django.shortcuts import render
from .form import TextForm
from django.http import JsonResponse
from .models import TextModel
# Create your views here.
from django.shortcuts import render
from django.forms.models import model_to_dict

def home(request):
	if request.method=='POST':
		form = TextForm(request.POST,request.FILES)
		if form.is_valid():
			print('form is valid')
			out=form.save()
			#cleaned_data is built in function but before that is_valid must be called
			output=form.cleaned_data['text']
			print(output)
			return JsonResponse({'text':output},status=200)
		else:
			print('form is invalid')
			return render(request,'home.html',{'form':form})
	else:
		form = TextForm()
		return render(request,'home.html',{'form':form})

