from django.shortcuts import render
from django.http import HttpResponse
# Create your views her
def uri(request):
	referer=request.META.get('HTTP_REFERER','no referer')
	agent=request.META.get('HTTP_USER_AGENT','no agent')
	ip=request.META.get('REMOTE_ADDR','no ip')
	return HttpResponse(referer+'<br/>'+agent+'<br/>'+ip)
def header(request):
	re=request.META.items()
	return render(request,'header.html',{'re':re})