from django import forms
class NameForm(forms.Form):
	myname=forms.CharField(label='my name',max_length=100)
	myage=forms.IntegerField(label='my age')
	myemail=forms.EmailField(label='my email',max_length=20)