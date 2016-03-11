from django.shortcuts import render
from django.http import HttpResponse
from app7.models import *
def a(request):
	aall=Author.objects.exclude(city='shanghai')
	ex=Author.objects.filter(city='shanghai')[0]
	a=Author.objects.all().order_by(('name')).values()
	sh=Author.objects.filter(id=3)
	te=Test.objects.filter(pk=2)
	return HttpResponse(a)
def age(request,year='333',province='xg'):
	return HttpResponse(province)
def page(request,page):
	page=str(page)
	# f=open('./templates/page3.html','w')
	return render(request,'page'+page+'.html')