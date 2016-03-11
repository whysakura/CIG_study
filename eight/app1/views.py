from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
#from django.http import HttpResponseRedirect

# Create your views here.
def show(request):
	#{% url 'add2' 4 5 %} 
	return HttpResponse(request.GET['a'])

def get(request,a,b):
	 return HttpResponse(int(a)+int(b))

def new_get(request,a,b):
	return HttpResponseRedirect(#重定向函数
	reverse('get',args=(a,b))
	)
def aa(request):
	return HttpResponseRedirect(reverse('bb'))

def app2(request):
	return HttpResponse('app2')