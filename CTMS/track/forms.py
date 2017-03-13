from django import forms

class Driver(forms.Form):
	id=forms.CharField(label='id:', max_length=100)
	fname =forms.CharField(label='First Name:', max_length=60)
	lname=forms.CharField(label='Last Name:',max_length=60)
	phone=forms.CharField(label='Phone Number:',max_length=10)
	email=forms.EmailField(label='email:',  max_length=60)
