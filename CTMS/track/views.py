from django.shortcuts import render, HttpResponse
from .forms import Driver

def reg_Driver(request):
	if request.method == 'POST':
		 form=Driver(request.POST)
		 if form.is_valid():
		 	id=form.cleaned_data['id']
		 	fname=form.cleaned_data['fname']
		 	lname=form.cleaned_data['lname']
		 	phone=form.cleaned_data['phone']
		 	email=form.cleaned_data['email']
		 	return HttpResponse('the form is ok')
	else:
		form=Driver()

	return render(request,'track/index.html', {'form':form})


