#3A车间设计

#更改：
# 1：改变库设计
# 2：增加站点输入料号和数目
# 3：改成一次发一个点。到达之后更改状态。




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
	if Order.objects.filter(order_sn=num):
		create_order()
	return num
def ask(request):
	or_num=create_order()
	line=request.GET.get('line','')
	gid=request.GET.get('gid','')
	count=request.GET.get('count','')
	if line==''or gid==''or count=='':
		print('缺少某个值返回0x01')
		return HttpResponse('0x01')
	if Order.objects.filter(line_id=line,order_state='未完成'):
		print('未完成')
		return HttpResponse('existed')
	# if Order.objects.all().count()>1000000:

	date=time.strftime('%Y/%m/%d %H:%M:%S')

	li_num=Linebody.objects.all().get(line_id=line)
	print(li_num)
	o=Order()
	o.line_id=li_num
	o.order_sn=or_num
	o.order_time=date
	# car=Car.objects.all().get(car_number='1')
	# o.car_number=car
	o.save()
	print('总订单数目'+str(Order.objects.all().count()))

	ordd=Order.objects.get(order_sn=or_num)
	goid=Goods.objects.get(goods_id=gid)
	o_de=Order_de()
	o_de.order_sn=ordd
	o_de.goods_id=goid
	o_de.goods_count=count
	o_de.save()


	return HttpResponse(create_order()+'<br/>'+line+'<br/>'+date)

#显示完成订单
def over_order(request):
	data=Order_de.objects.select_related().all().values(
		'order_sn__line_id',
		'order_sn__order_sn',
		'order_sn__order_state',
		'order_sn__line_id__station_number',
		'order_sn__order_time',
		'order_sn__car_number',
		'order_sn__car_number__car_state__sta_name',
		'order_sn__down_time',
		'order_sn__finish_time',
		'order_sn__total_time',
		'goods_id',
		'goods_count',
		'goods_id__goods_name',
		'goods_id__goods_station',
		).filter(order_sn__order_state='完成')
	return render(request,'over.html',locals())

#显示未完成订单
def show_order(request):
	data=Order_de.objects.select_related().all().values(
		'order_sn__line_id',
		'order_sn__order_sn',
		'order_sn__order_state',
		'order_sn__line_id__station_number',
		'order_sn__order_time',
		'order_sn__car_number',
		'order_sn__car_number__car_state__sta_name',
		'order_sn__down_time',
		# 'order_sn__finish_time',
		# 'order_sn__total_time',
		'goods_id',
		'goods_count',
		'goods_id__goods_name',
		'goods_id__goods_station',
		).filter(order_sn__order_state='未完成')
	return render(request,'show.html',locals())
	# return HttpResponse(data)
#ajax数据
def show_data(request):
	data=Order_de.objects.select_related().all().values(
		'order_sn__line_id',
		'order_sn__order_sn',
		'order_sn__order_state',
		'order_sn__line_id__station_number',
		'order_sn__order_time',
		'order_sn__car_number',
		'order_sn__car_number__car_state__sta_name',
		'order_sn__down_time',
		# 'order_sn__total_time',
		'goods_id',
		'goods_count',
		'goods_id__goods_name',
		'goods_id__goods_type',
		'goods_id__goods_station',
		).filter(order_sn__order_state='未完成')
	data=json.dumps(list(data))
	# print(data)
	return HttpResponse(data)

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
			if Car.objects.filter(car_number=num,car_state='3'):
				line_number=order.line_id#线体号
				zd=Linebody.objects.filter(line_id=line_number)[0]
				print('站@点'+zd.station_number)
				return HttpResponse(zd.station_number)
			#物料站点号
			if Car.objects.filter(car_number=num,car_state='1'):
				gid=order.order_de_set.all().values()[0]['goods_id_id']
				sn=Goods.objects.filter(goods_id=gid)[0]#order_sn
				print('物@料'+sn.goods_station)
				return HttpResponse(sn.goods_station)
			# if Car.objects.filter(car_number=num,car_state='0'):
			# 	order=Order.objects.filter(car_number=num,order_state='未完成').order_by('id')[0]
			# 	#状态改为1
			# 	sta=State.objects.all().get(sta_number='1')
			# 	c=Car.objects.get(car_number=num)
			# 	c.car_state=sta
			# 	c.save()
			# 	#物料站点号
			# 	gid=order.order_de_set.all().values()[0]['goods_id_id']
			# 	sn=Goods.objects.filter(goods_id=gid)[0]#order_sn
			# 	print('綫體'+sn.goods_station)
			# 	return HttpResponse(sn.goods_station)
			if Car.objects.filter(car_number=num,car_state='2'):
				order=Order.objects.filter(car_number=num,order_state='未完成').order_by('id')[0]
				#状态改为1
				sta=State.objects.all().get(sta_number='3')
				c=Car.objects.get(car_number=num)
				c.car_state=sta
				c.save()
				#站点号
				line_number=order.line_id#线体号
				zd=Linebody.objects.filter(line_id=line_number)[0]
				print('站点'+zd.station_number)
				return HttpResponse(zd.station_number)
		elif Car.objects.filter(car_number=num,car_state='0'):
			if Order.objects.filter(order_state="未完成",car_number=None):
				order=Order.objects.filter(order_state="未完成",car_number=None).order_by('id')[0]
				#判断小车停的前后位置或者是让小车到点之后才发状态0
				car=Car.objects.all().get(car_number=num)
				order.car_number=car
				order.save()
				print('create ok')
				#物料站点号
				gid=order.order_de_set.all().values()[0]['goods_id_id']
				sn=Goods.objects.filter(goods_id=gid)[0]#order_sn
				print('物料'+sn.goods_station)
				
					if sn.goods_station=='0x01':
						sta=State.objects.all().get(sta_number='3')
						c=Car.objects.get(car_number=num)
						c.car_state=sta
						c.save()
						o=Order.objects.get(car_number=num,order_state="未完成")
						if Order.objects.filter(down_time=''):
							o.down_time=tm
						o.save()
						line_number=order.line_id#线体号
						zd=Linebody.objects.filter(line_id=line_number)[0]
						print('由于在取料点1所以去站@点'+zd.station_number)
						return HttpResponse(zd.station_number)
				#状态改为1
				sta=State.objects.all().get(sta_number='1')
				c=Car.objects.get(car_number=num)
				c.car_state=sta
				c.save()
				return HttpResponse(sn.goods_station)
			return HttpResponse('0x01')
		else:
			print('no order')
			return HttpResponse('')


	elif int(state)==2:
		#只要在中途判断有没有小车状态为0的。
		# if Car.objects.filter(car_number=num,car_state='0'):
		# 	if Order.objects.filter(order_state="未完成",car_number=None):

		return HttpResponse('')



	elif int(state)==4:
		#完成送料
		if Car.objects.filter(car_number=num,car_state='3'):
			o=Order.objects.get(car_number=num,order_state="未完成")
			# print(type(order))
			o.finish_time=tm
			o.order_state='完成'
			# print(type(o.order_time))
			od=time.mktime(time.strptime(o.order_time,'%Y/%m/%d %H:%M:%S'))
			fi=time.mktime(time.strptime(tm,'%Y/%m/%d %H:%M:%S'))
			if float(fi-od)<3600:
				fen=time.localtime(fi-od)
				time_cha=time.strftime('%M:%S',fen)
			else:
				fen=time.localtime(fi-od)
				time_cha=time.strftime('%H:%M:%S',fen)
			o.total_time=time_cha
			o.save()
			sta=State.objects.all().get(sta_number='0')
			c=Car.objects.get(car_number=num)
			c.car_state=sta
			c.save()

			print('送料完成')
			#并给它一个返回指令
			if Order.objects.filter(order_state='未完成').count()==0:
				print('没订单状态改为0返回0x01')
				sta=State.objects.all().get(sta_number='4')
				c=Car.objects.get(car_number=num)
				c.car_state=sta
				c.save()
				return HttpResponse('')
			return HttpResponse('')
		elif Car.objects.filter(car_number=num,car_state='1'):
			sta=State.objects.all().get(sta_number='2')
			c=Car.objects.get(car_number=num)
			c.car_state=sta
			c.save()
			o=Order.objects.get(car_number=num,order_state="未完成")
			if Order.objects.filter(down_time=''):
				o.down_time=tm
			o.save()
			print('装料')
			return HttpResponse('taking')
		else:
			print('状态四错误')
			return HttpResponse('')
	else:
		print('return or send error')
		return HttpResponse('return')

