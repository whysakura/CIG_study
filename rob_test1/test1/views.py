#3A车间设计


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
	if line=='':
		return HttpResponse('plase add line')
	if Order.objects.filter(line_number=line,order_state='未完成'):
		return HttpResponse('线体'+line+'is existed')
	date=time.strftime('%Y/%m/%d %H:%M:%S')

	li_num=Linebody.objects.all().get(line_number=line)
	print(li_num)
	o=Order()
	o.line_number=li_num
	o.order_number=or_num
	o.order_time=date
	o.save()
	print(Order.objects.all().values())
	#选择小车，可能还要判断小车位置的前后
	# cars=Car.objects.filter(car_state__sta_number='0')
	# print(cars.count())
	# ccount=cars.count()
	# if cars==1:
	return HttpResponse(or_num+'<br/>'+line+'<br/>'+date)

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

#显示完成订单
def over_order(request):
	data=Order.objects.select_related().filter(order_state='完成').values(
		'order_number',
		'line_number',
		# 'line_number__station_number',
		'line_number__material_number',
		'line_number__material_number__mat_name',
		# 'line_number__material_number__mat_type',
		'line_number__material_number__mat_count',
		'order_time',
		'order_state',
		'car_number',
		'down_time',
		'finish_time',
		# 'car_number__car_state__sta_name',
		)
	time_cha=[]
	for i in data:
		od=time.mktime(time.strptime(i['order_time'],'%Y/%m/%d %H:%M:%S'))

		fi=time.mktime(time.strptime(i['finish_time'],'%Y/%m/%d %H:%M:%S'))
		if float(fi-od)<3600:
			fen=time.localtime(fi-od)
			time_cha.append(time.strftime('%M:%S',fen))
		else:
			fen=time.localtime(fi-od)
			time_cha.append(time.strftime('%H:%M:%S',fen))
	# print(time.strftime())
	# print(time_cha)
	return render(request,'over.html',locals())

#显示未完成订单
def show_order(request):
	data=Order.objects.select_related().filter(order_state='未完成').values(
		'order_number',
		'line_number',
		'line_number__station_number',#__station_code
		'line_number__material_number',
		'line_number__material_number__mat_name',
		'line_number__material_number__mat_type',
		'line_number__material_number__mat_count',
		'order_time',
		'order_state',
		'car_number',
		'down_time',
		'car_number__car_state__sta_name',
		)
	# line=data[0]['line_number']
	# linebody=Linebody.objects.filter(line_number=line).values()
	# d=chain(data,linebody)
	print(data)
	return render(request,'show.html',locals())
#ajax数据
def show_data(request):
	data=Order.objects.select_related().filter(order_state='未完成').values(
		'order_number',
		'line_number',
		'line_number__station_number',#__station_code
		'line_number__material_number',
		'line_number__material_number__mat_name',
		'line_number__material_number__mat_type',
		'line_number__material_number__mat_count',
		'order_time',
		'order_state',
		'car_number',
		'down_time',
		'car_number__car_state__sta_name',
		)
	data=json.dumps(list(data))
	return HttpResponse(data)
#提交选择小车
# def get_car(request):
# 	a=request.POST.get('order_id','')
# 	b=request.POST.get('car_number','')
# 	tm=time.strftime('%Y/%m/%d %H:%M:%S')
# 	car=Car.objects.all().get(car_number=b)
# 	o=Order.objects.get(id=a)
# 	o.car_number=car
# 	o.down_time=tm
# 	o.save()
# 	#改变小车状态
# 	# tm=time.strftime('%Y/%m/%d %H:%M:%S')
# 	sta=State.objects.all().get(sta_number='1')
# 	c=Car.objects.get(car_number=b)
# 	c.car_state=sta
# 	c.save()
# 	return HttpResponse('小车'+b+'马上配送')
# #显示小车状态
# def show_car(request,a):
# 	car_data=Car.objects.select_related().filter(car_number=a).values('car_number','car_state__sta_name','down_time')
# 	return render(request,'car.html',locals())
#接受小车状态
def car_sta(request):
	car_data=json.loads(request.body.decode('utf-8'))
	state=car_data['car_state']
	num=car_data['car_number']
	# pos=car_data['position']
	# print(state,car_data,pos)
	tm=time.strftime('%Y/%m/%d %H:%M:%S')
	if int(state)==0:

	#判断是不是重复发送0
		if Order.objects.filter(order_state="未完成",car_number=num):
			order=Order.objects.filter(order_state="未完成",car_number=num).order_by('id')[0]
			#返回站点代码
			line_number=order.line_number#线体号
			zd=Linebody.objects.select_related().filter(line_number=line_number).values('station_number__station_code',)
			zhan=zd[0]['station_number__station_code']
			#物料站点号
			wuliao=Linebody.objects.get(line_number=line_number)
			print(wuliao.wuliao_id+','+zhan)
			return HttpResponse(wuliao.wuliao_id+','+zhan)

	#给小车分配任务 并    判断小车停的前后位置
		if Order.objects.filter(order_state="未完成",car_number=None):
			order=Order.objects.filter(order_state="未完成",car_number=None).order_by('id')[0]
			print('线体',order.line_number)

			#判断小车停的前后位置或者是让小车到点之后才发状态0
			car=Car.objects.all().get(car_number=num)
			order.car_number=car
			order.save()

			sta=State.objects.all().get(sta_number='1')
			c=Car.objects.get(car_number=num)
			c.car_state=sta
			c.save()

			#返回站点代码
			line_number=order.line_number#线体号
			zd=Linebody.objects.select_related().filter(line_number=line_number).values('station_number__station_code',)
			zhan=zd[0]['station_number__station_code']
			#物料站点号
			wuliao=Linebody.objects.get(line_number=line_number)
			print(wuliao.wuliao_id+','+zhan)
			return HttpResponse(wuliao.wuliao_id+','+zhan)
		else:
			print('no order')
			return HttpResponse('no order ')
	elif int(state)==2:
		#送料
		if Car.objects.filter(car_number=num,car_state='2'):
			print('taking')
			return HttpResponse('taking')
		sta=State.objects.all().get(sta_number='2')
		c=Car.objects.get(car_number=num)
		c.car_state=sta
		c.save()
		o=Order.objects.get(car_number=num,order_state="未完成")
		o.down_time=tm
		o.save()
		print(tm)
		return HttpResponse('taking')

	# elif int(state)==3:
	# 	#送料
		
	# 	sta=State.objects.all().get(sta_number='3')
	# 	c=Car.objects.get(car_number=num)
	# 	c.car_state=sta
	# 	c.save()
	# 	print('songliao')
	# 	return HttpResponse('taking')
	elif int(state)==4:
		#完成送料
		o=Order.objects.get(car_number=num,order_state="未完成")
		# print(type(order))
		o.finish_time=tm
		o.order_state='完成'
		o.save()
		sta=State.objects.all().get(sta_number='0')
		c=Car.objects.get(car_number=num)
		c.car_state=sta
		c.save()
		# time.sleep(5)
		print('return code 0')
		#并给它一个返回指令
		return HttpResponse('0')
	else:
		#装料
		# sta=State.objects.all().get(sta_number='1')
		# c=Car.objects.get(car_number=num)
		# c.car_state=sta
		# c.save()
		print('return or send error')
		return HttpResponse('return')

