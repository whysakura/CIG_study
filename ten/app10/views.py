from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import *
# Create your views here.
def sh(request):
	tm=Book.objects.all().values()
	if Book.objects.all().count() > 3:
		Book.objects.all().delete()
	return HttpResponse(tm)