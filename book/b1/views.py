from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import *
from .forms import *
import json
# Create your views here.
def add(request):
	data={ "people": [{ "firstName": "Brett", "lastName":"McLaughlin", "email": "aaaa" },
{ "firstName": "Jason", "lastName":"Hunter", "email": "bbbb"},
{ "firstName": "Elliotte", "lastName":"Harold", "email": "cccc" }
]}
	print(repr(data))
	data_string=json.dumps(data)
	print(type(data_string))
	data_json=json.loads(data_string)
	print(data_json['people'])
	return HttpResponse(data_json['people'][0]['email'])
def added(request):
	return render(request,'added.html')
	# error=[]
	# mname=request.POST.get('myname','1')
	# return HttpResponse(mname)
	# mage=request.POST.get('myage','')
	# memail=request.POST.get('myemail','')
	# if mname=='' :
	# 	error.append('no name')
	# if mage=='' :
	# 	error.append('no age')
	# if memail=='' or '@' not in memail :
	# 	error.append('no email or not have @')
	# if error:
	# 	return render(request,'add.html',{'error':error,'mname':mname,'mage':mage,'memail':memail})
	# mydata=Mydata(name=mname,age=mage,email=memail)
	# mydata.save()
	# return HttpResponse(mname+'<br/>'+mage+'<br/>'+memail+'<br/>save ok')
# def added(request):
# 	form=NameForm(request.POST)
# 	if form.is_valid():
# 		d=form.cleaned_data
# 		return HttpResponse(d['myage'])
# 	else:
# 		return render(request,'add.html',{'form':form})
# POST /added/ HTTP/1.1
# Host:172.30.2.217
# Content-Type:application/x-www-form-urlencoded
# Content-Length:10
# def pos(request, station_id, cig_sn='CIGG01020304', pcba_code='110-00007-21', laser_sn='145J7243266B51', test_tray='0001'):
# 	data = {
# 	'station_id': station_id,
# 	'tray_sn':test_tray,
# 	'pcba_info': {
# 	'cig_sn': cig_sn,
# 	'pcba_code': pcba_code,
# 	'laser_sn': laser_sn,
# 	},
# 	}
# 	r = requests.post("http://172.30.2.217/added", json.dumps(data))
# 	print(json.dumps(data))
# 	if __name__=='__main__':
# 		print(r)
# 	return HttpResponse(r)
def gt(request):
	if request.method == 'POST':
		data=json.loads(request.body.decode('ASCII'))
	print(data['sta'])
	return HttpResponse(data['sta'])
def pt(request):
	return render(request,'add.html')