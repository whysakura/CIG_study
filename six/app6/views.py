from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def show(request,a,b):
	now =datetime.datetime.now()
	#assert False
	html="<html><body>It is now %s,and %s,or %s</body></html>"%(now,a,b)
	return HttpResponse(html)

def index(request):
	return render(request,'index.html')
