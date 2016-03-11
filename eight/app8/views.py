from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from itertools import chain
import time
def app8(request):
	return HttpResponse('23333')
def app3(request):
	pa=request.GET.get('page','1')
	aurl=request.get_full_path()#获取带参数URL
	url=request.path#获取不带参数URL
	host=request.get_host()#获取主机地址
	#request.is_secure(),表示如果通过HTTPS访问，则此方法返回True， 否则返回False
	return render(request,'page'+pa+'.html')#?????
def show_data(request):
	data1=Data_1.objects.all().order_by('id').reverse().values()[:10]
	data2=Data_2.objects.all().order_by('id').reverse().values()[:10]
	data3=Data_3.objects.all().order_by('id').reverse().values()[:10]
	data4=Data_4.objects.all().order_by('id').reverse().values()[:10]

	# data=chain(data1,data2)
	return render(request,'data.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4})
	# return HttpResponse(data)
def inn(request):
	para=request.GET.get('robot','')#发参数robot几号
	sta=request.GET.get('state','100')#发机器状态码state
	if para=='' or sta=='':
		return HttpResponse('请输入参数')
	data='Data_'+para#获取哪个机器
	timee=time.strftime("%Y-%m-%d %H:%M:%S")
	if int(para)>=1 and int(para)<=4 :
		if eval(data).objects.filter(date=timee):
			return HttpResponse('已经存在')
		roo=eval(data)(date=timee,state=sta,robot=para)
		roo.save()
			# 	#接下来就是判断它该做什么了。。。。。
		return HttpResponse('robot'+para+':save ok')#显示多少料
	else:
		return HttpResponse('error')
	# if para=='2':
	# 	if Data_2.objects.filter(date=timee):
	# 		return HttpResponse('已经存在')
	# 	roo=eval(ro)(date=timee,state=sta)
	# 	roo.save()
	# 	return HttpResponse(para)
	# if para=='3':
	# 	if Data_3.objects.filter(date=timee):
	# 		return HttpResponse('已经存在')
	# 	roo=Data_3(date=timee,state=sta)
	# 	roo.save()
	# 	return HttpResponse(para)
	# if para=='4':
	# 	if Data_4.objects.filter(date=timee):
	# 		return HttpResponse('已经存在')
	# 	roo=Data_4(date=timee,state=sta)
	# 	roo.save()
	# 	return HttpResponse(para)
	# a1=ro(date=timee,state=sta)
	# if Data.objects.filter(name=para):
	# 	return HttpResponse('已经存在')
	# else:
	# 	person=Data(name=para,age=agee)
	# 	person.save()
	# 	#接下来就是判断它该做什么了。。。。。
	# 	return HttpResponse('yes'+para)
def fanhui(request):
	page=request.GET.get('page','0')
	if page=='0':
		return HttpResponse('请输入参数')
	shuju=Order.objects.all()
	for i in shuju:
		print(i.order,page)
		if str(i.name)==page:
			return HttpResponse(i.order)
	return HttpResponse('nodata')
	# if page=='a'
	# 	return HttpResponse('no data')
	# if shuju=Person.objects.get('age'=page)
	# 	return HttpResponse(shuju)
	# return HttpResponse('no page')