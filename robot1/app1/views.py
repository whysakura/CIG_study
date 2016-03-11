from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import time,math
import json
from django.core import serializers
from operator import itemgetter
# Create your views here.
def test(request):
	idd=Robot_1.objects.all().count()
	idd=int(idd)-10
	if idd<=10:
		return HttpResponse('plase add data')
	data1=Robot_1.objects.all()[idd:]
	data=[]
	for i in data1:
		data.append(i.date)
		data.append(i.state)
		
	# if Robot_1.objects.all().count()>=1500:
	# 	Robot_1.objects.all().delete()
	return render(request,'show_new.html',{'data':data})
	# return HttpResponse(data1)
def car_sta(request):
	if request.method=='POST':
		
		# robot=json.loads(request.body.decode('utf-8'))['rob']
		# sta=json.loads(request.body.decode('utf-8'))['sta']
		car_data=json.loads(request.body.decode('utf-8'))
		robot=car_data['car_number']
		sta=int(car_data['car_state'])/2
		print(robot+'?'+str(sta))
	else:
		return HttpResponse('not post')
	rob='Robot_'+robot#获取机器号
	now_time='Now_time_'+robot#机器时间戳
	sec='Second_'+robot
	tmc=time.time()#时间戳
	tm=time.strftime('%m/%d %H:%M:%S')#格式时间戳
	if eval(now_time).objects.all().count()>=1:#计算时间差并存入second库
		# num=eval(now_time).objects.all().count()-1
		lastone=eval(now_time).objects.all().values().last()['time']
		lastone=float(lastone)
		cha=round(tmc-lastone)#时间差
		s=eval(sec)(sec=cha)
		s.save()
		# print(type(lastone))
		# return HttpResponse(lastone)
	tmc=str(tmc)
	t=eval(now_time)(time=tmc)#存储时间戳
	t.save()
	d=eval(rob)(date=tm,state=sta)#存储信息
	d.save()
	return HttpResponse(sta)
def ceshi(request):
	idd=Robot_1.objects.all().count()
	if idd<=10:
		return HttpResponse('plase add data')
	idd=int(idd)-10
	data1=Robot_1.objects.all()[idd:]
	data=[]
	for i in data1:
		data.append(i.date)
		data.append(i.state)
	if Robot_1.objects.all().count()>=1500020000:
		Robot_1.objects.all().delete()
	idd=idd+10
	err_num=Robot_1.objects.filter(state=0).count()
	err_rate=round((err_num/idd)*100)
	return render(request,'ceshi.html',locals())
	# return HttpResponse(data1)
def err_show(request):
	err_data=Robot_1.objects.filter(state=0).values()
	return render(request,'err_show.html',locals())
def show(request,rob):
	# rob=request.GET.get('robot','')
	robot='Robot_'+rob
	sec='Second_'+rob
	now_time='Now_time_'+rob
	idd=eval(robot).objects.all().count()
	if idd<10:
		return HttpResponse('plase add data')
	idd=int(idd)-10
	print(eval(robot).objects.all().values().last())
	data=serializers.serialize('json',eval(robot).objects.all()[idd:])
	if eval(robot).objects.all().count()>=1000000:
		eval(robot).objects.all().delete()
		eval(sec).objects.all().delete()
		eval(now_time).objects.all().delete()
	g=eval(sec).objects.exclude(sec__in=[0,1,2,3,4,5]).count()
	a=eval(sec).objects.filter(sec=0).count()
	b=eval(sec).objects.filter(sec=1).count()
	c=eval(sec).objects.filter(sec=2).count()
	d=eval(sec).objects.filter(sec=3).count()
	e=eval(sec).objects.filter(sec=4).count()
	f=eval(sec).objects.filter(sec=5).count()
	couu=eval(robot).objects.all().count()
	a1=round((a/couu)*100,2)
	b1=round((b/couu)*100,2)
	c1=round((c/couu)*100,2)
	d1=round((d/couu)*100,2)
	e1=round((e/couu)*100,2)
	f1=round((f/couu)*100,2)
	g1=round((g/couu)*100,2)
	print(a,b,c,d,e,f,g)
	h=eval(sec).objects.exclude(sec__in=[0,1,2,3,4,5]).values()
	dit=[]
	for i in h:
		dit.append(i['sec'])
	dit=list(set(dit))
	cou=len(dit)
	dit.sort(key=int)
	# print(dit)
	st=[]
	for y in range(cou):
		st.append([])
		st[y].append(eval(sec).objects.filter(sec=dit[int(y)]).count())
		if int(dit[y])<3600:
			dit[y]=time.strftime("%MM %SS",time.localtime(int(dit[y])))
		else:
			aaa=int(dit[y])
			bbb=math.floor(aaa/3600)
			dit[y]=str(bbb)+str(time.strftime(":%M:%S",time.localtime(int(dit[y]))))
		st[y].append(dit[y])
	
	# print(st)
	return render(request,'test.html',locals())
def timee(request):
	num=Now_time_1.objects.all().count()
	a=0
	b=0
	c=0
	d=0
	e=0
	f=0
	g=0
	for i in range(num-1):
		tm1=Now_time_1.objects.all().order_by('-time')[i].time
		tm2=Now_time_1.objects.all().order_by('-time')[i+1].time
		cha=round(float(tm1)-float(tm2))
		if cha==0:
			a=a+1
		if cha==1:
			b=b+1
		if cha==2:
			c=c+1
		if cha==3:
			d=d+1
		if cha==4:
			e=e+1
		if cha==5:
			f=f+1
		if cha>5:
			g=g+1
	return render(request,'test.html',locals())