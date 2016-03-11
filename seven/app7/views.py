from django.shortcuts import render
# from django.template import Template,Context
from django.http import HttpResponse
# from django.template.loader import get_template
from .models import *
import datetime
# Create your views here.
def tem(request):
	current_date=datetime.datetime.now()
	late="dddd"
	# fp=open('E:/wrd/seven/app7/templates/tem.html')
	# t=Template(fp.read())
	# fp.close()
	# html=t.render(Context({'current_date':now}))
	# return HttpResponse(html)
	return render(request,'jc.html',locals())
	# now=datetime.datetime.now()
	# t=get_template('tem.html')
	# html=t.render(Context({'current_date':now}))
	# return HttpResponse(html)
def show(request):
	au=Author.objects.all()
	x=[]
	for a in au:
		print(a)
		x.append(a)
	#return HttpResponse(x)
	return render(request,'show.html',{'au':au})
def add(request):
	book=Author(name='王五',city='shanghai',email='3232322@qq.com')
	book.save()
	return HttpResponse('yes')
def app4(request):
	return HttpResponse("woshi app7")