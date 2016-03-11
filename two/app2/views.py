#coding: utf-8
from django.shortcuts import render
#from django.http import HttpResponse这个不能写
# Create your views here.

def aa(request,a,b):
	list=[a,b]
	aabb=request.GET['b']
	return render(request,'app2/home.html',{'list':list,'aaa':aabb})
	
def home1(request):
	tushu={'site':'三百六十行','content':'行行出状元'}
	return render(request,'app2/home1.html',{'tushua':tushu})