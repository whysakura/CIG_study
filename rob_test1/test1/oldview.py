from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json,time,random
from itertools import chain
from django.core import serializers

# Create your views here.
#创建订单号
def create_order():
	a=time.strftime('%Y%m%d%H%M%S')
	a='CIG'+a
	items=['1','2','3','4','5','6','7','8','9','a','s','d','f','g','h','j','k','q','w','e','r','t','y','u','i','p','z','x','c','v','b','n','m']
	random.shuffle(items)
	num=a+str('').join(items)[0:5]
	if Order.objects.filter(order_number=num):
		create_order()
	return num
def ask(request):
	or_num=create_order()
	line=request.GET.get('line','')
	date=time.strftime('%Y/%m/%d %H:%M:%S')
	if line=='':
		return HttpResponse('plase add line')
	li_num=Linebody.objects.all().get(line_number=line)
	o=Order(order_number=or_num,line_number=li_num,order_time=date)
	o.save()
	return HttpResponse(create_order()+'<br/>'+line+'<br/>'+date)

# def inn(request):
# 	data=json.loads(request.body.decode('utf-8'))
# 	station=data['Station']
# 	material=data['Material']
# 	car=data['Car']
# 	linebody=data['Linebody']
# 	# for k,v in data.items():
# 	# 	for k1,v1 in v.items():
# 	# 		if len(v1)==0:
# 	# 			return HttpResponse(k1+'->no data')
# 	# 		print('%s=%s' %(k1,v1))
# 	ss=Station(**station)
# 	ss.save()
# 	mm=Material(**material)
# 	mm.save()
# 	ll=Linebody(**linebody)
# 	ll.save()

# 	state=car['car_state']
# 	sta_class=State.objects.get(sta_number=state)
# 	if int(state)>2:
# 		return HttpResponse('car_state is big')
# 	# print(type(sta_class))
# 	cc=Car(car_name=car['car_name'],car_state=sta_class,down_time=car['down_time'],car_sign=car['car_sign'])
# 	cc.save()
# 	return HttpResponse('inn ok')

#显示订单
def show_order(request):
	data=Order.objects.select_related().filter(order_state='未完成').values(
		'id',
		'order_number',
		'line_number',
		'line_number__station_number',
		'line_number__material_number',
		'line_number__material_number__mat_name',
		'line_number__material_number__mat_type',
		'line_number__material_number__mat_count',
		'order_time',
		'order_state',
		'car_number',
		)
	# line=data[0]['line_number']
	# linebody=Linebody.objects.filter(line_number=line).values()
	# d=chain(data,linebody)
	print(data)
	return render(request,'show.html',locals())
#ajax数据
def show_data(request):
	data=Order.objects.select_related().filter(order_state='未完成').values(
		'id',
		'order_number',
		'line_number',
		'line_number__station_number',
		'line_number__material_number',
		'line_number__material_number__mat_name',
		'line_number__material_number__mat_type',
		'line_number__material_number__mat_count',
		'order_time',
		'order_state',
		'car_number',
		)
	data=json.dumps(list(data))
	return HttpResponse(data)
#提交选择小车
def get_car(request):
	a=request.POST.get('order_id','')
	b=request.POST.get('car_number','')
	car=Car.objects.all().get(car_number=b)
	o=Order.objects.get(id=a)
	o.car_number=car
	o.save()
	#改变小车状态
	tm=time.strftime('%Y/%m/%d %H:%M:%S')
	sta=State.objects.all().get(sta_number='1')
	c=Car.objects.get(car_number=b)
	c.car_state=sta
	c.down_time=tm
	c.save()
	return HttpResponse('小车'+b+'马上配送')
#显示小车状态
def show_car(request,a):
	car_data=Car.objects.select_related().filter(car_number=a).values('car_number','car_state__sta_name','down_time')
	return render(request,'car.html',locals())
#接受小车状态
def car_sta(request):
	car_data=json.loads(request.body.decode('utf-8'))
	state=car_data['car_state']
	num=car_data['car_number']
	print(state,car_data)
	tm=time.strftime('%Y/%m/%d %H:%M:%S')
	if int(state)==0:
	#给小车发送消息并
		order=Order.objects.filter(car_number=num,order_state="未完成")
		# print(order[0].line_number)
		line_num=order[0].line_number
		station=Linebody.objects.filter(line_number=line_num)
		# print(station[0].station_number)
		zhandian=station[0].station_number#站点代号
		print(zhandian)
		return HttpResponse(zhandian)
	if int(state)==2:
		sta=State.objects.all().get(sta_number='2')
		c=Car.objects.get(car_number=num)
		c.car_state=sta
		c.save()
	elif int(state)==3:
		o=Order.objects.get(car_number=num,order_state="未完成")
		# print(type(order))
		o.finish_time=tm
		o.order_state='完成'
		o.save()
		sta=State.objects.all().get(sta_number='0')
		c=Car.objects.get(car_number=num)
		c.car_state=sta
		c.save()

		return HttpResponse('ok')
	else:
		return HttpResponse('taking')

