#3B车间设计





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
	a='CIG3B_pcb'+a
	items=['1','2','3','4','5','6','7','8','9','a','s','d','f','g','h','j','k','q','w','e','r','t','y','u','i','p','z','x','c','v','b','n','m']
	random.shuffle(items)
	num=a+str('').join(items)[0:5]
	if OrderPcb.objects.filter(order_sn=num):
		create_order()
	return num
def ask(request):
	data=json.loads(request.body.decode('utf-8'))
	or_num=create_order()
	line=data['0']['line']
	wtype=data['0']['type']
	if wtype=='1' and len(data)==2:
		print('送完成品的只有一个点')
		return HttpResponse('error')
	if OrderPcb.objects.filter(line_id=line,order_state='未完成'):
		print('未完成')
		return HttpResponse('existed')
	for a,b in data.items():
		print(b['count'],b['line'],b['gid'])
		line=b['line']
		gid=b['gid']
		count=b['count']
		if line==''or gid==''or count=='':
			print('返回0x01，状态改为5')
			sta=State.objects.all().get(sta_number='5')
			c=Car.objects.get(car_number=num)
			c.car_state=sta
			c.save()
			return HttpResponse('0x01')
		# if OrderPcb.objects.all().count()>1000000:
		if not OrderPcb.objects.filter(order_sn=or_num):
			date=time.strftime('%Y/%m/%d %H:%M:%S')
			li_num=Linebody.objects.all().get(line_id=line)
			print(li_num)
			o=OrderPcb()
			o.line_id=li_num
			o.order_sn=or_num
			o.order_time=date
			o.work_type=wtype
			o.save()
			print('总订单数目'+str(OrderPcb.objects.all().count()))

		ordd=OrderPcb.objects.get(order_sn=or_num)
		goid=Goods.objects.get(goods_id=gid)
		o_de=OrderPcb_de()
		o_de.order_sn=ordd
		o_de.goods_id=goid
		o_de.goods_count=count
		o_de.save()
	return HttpResponse(or_num+'<br/>'+line+'<br/>'+date)

#显示小车路线
def show_car(request):
	#返回所需数据
	# data=OrderPcb_de.objects.select_related().all().values(
	# 	'goods_id__goods_name',
	# 	'goods_count',
	# 	'goods_id__goods_station',
	# 	'order_sn__car_number',
	# 	'order_sn__car_number__car_state__sta_name',
	# 	'order_sn__car_number__car_mark',
	# 	# 'order_sn__car_number__car_mark__mark_state',
	# 	'order_sn__line_id__station_number',
	# 	).filter(order_sn__order_state='未完成')
	# if len(data)==0:
	# 	data=Car.objects.select_related().all().values(
	# 		'car_number',
	# 		'car_state__sta_name',
	# 		'car_mark',
	# 		# 'car_mark__mark_state',
	# 		).filter(car_number='1')
	# 	data=json.dumps(list(data),ensure_ascii=False)
	# 	return HttpResponse(data)
	# data=Mark.objects.select_related().all().values(
	# 	'mark_id','mark_state',
	# 	'next_main__mark_state',
	# 	).filter(mark_id='0x01')
	

	# lis=[]
	# for i in data:
	# 	a=[]
	# 	a.append(i)
	# 	lis.append(a)
	# print(lis)

	#转换为jsonstr

	#转为json list
	# data=json.loads(data)
	# print(type(data))	



	#修改版
	#返回所需数据
	lists=[]
	lists.append(5)
	car=Car.objects.get(car_number=str('5'))
	data=Car.objects.select_related().all().values(
			'car_state__sta_name',
			'car_mark',
			'distination',
			).filter(car_number=str('5'))
	lists.append(data[0]['car_state__sta_name'])
	lists.append(data[0]['car_mark'])
	lists.append(data[0]['distination'])
	data=json.dumps(list(lists),ensure_ascii=False)
	return HttpResponse(data)



#显示完成订单
def over_order(request):
	data=OrderPcb_de.objects.select_related().all().values(
		'order_sn__line_id',
		'order_sn__order_sn',
		'order_sn__order_state',
		'order_sn__line_id__station_number',
		'order_sn__order_time',
		'order_sn__car_number',
		'order_sn__car_number__car_state__sta_name',
		'order_sn__work_type',
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
	data=OrderPcb_de.objects.select_related().all().values(
		'order_sn__line_id',
		'order_sn__order_sn',
		'order_sn__order_state',
		'order_sn__line_id__station_number',
		'order_sn__order_time',
		'order_sn__car_number',
		'order_sn__car_number__car_state__sta_name',
		'order_sn__work_type',
		# 'order_sn__finish_time',
		# 'order_sn__total_time',
		'goods_id',
		'goods_count',
		'goods_id__goods_name',
		'goods_id__goods_station',
		).filter(order_sn__order_state='未完成')
	return render(request,'pcbshow.html',locals())
	# return HttpResponse(data)
#ajax数据
def show_data(request):
	data=OrderPcb_de.objects.select_related().all().values(
		'order_sn__line_id',
		'order_sn__order_sn',
		'order_sn__order_state',
		'order_sn__line_id__station_number',
		'order_sn__order_time',
		'order_sn__car_number',
		'order_sn__car_number__car_state__sta_name',
		'order_sn__work_type',
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
		if OrderPcb.objects.filter(order_state="未完成",car_number=num):
			order=OrderPcb.objects.filter(order_state="未完成",car_number=num).order_by('id')[0]
			#返回站点代码
			if Car.objects.filter(car_number=num,car_state='3'):
				#先判断是哪个工作类型
				if OrderPcb.objects.get(order_state="未完成",car_number=num).work_type=='1':
					#物料站点号
					
					print('再X去完成品地点0x03')
					#存入小车下一个目的地
					Car.objects.filter(car_number=num).update(distination='0x03')
					return HttpResponse('0x03')
				else:
					#站点号
					line_number=order.line_id#线体号
					zd=Linebody.objects.filter(line_id=line_number)[0]
					print('站x点'+zd.station_number)
					#存入小车下一个目的地
					Car.objects.filter(car_number=num).update(distination=zd.station_number)
					return HttpResponse(zd.station_number)


			#如果重复发1，判断工作类型
			if Car.objects.filter(car_number=num,car_state='1'):
				#返回站点
				if OrderPcb.objects.get(order_state="未完成",car_number=num).work_type=='1':
					line_number=order.line_id#线体号
					zd=Linebody.objects.filter(line_id=line_number)[0]
					print('先去站点'+zd.station_number)
					#存入小车下一个目的地
					Car.objects.filter(car_number=num).update(distination=zd.station_number)
					return HttpResponse(zd.station_number)
				else:
					#物料站点号
					gid=order.orderpcb_de_set.filter(order_state='0').values().order_by('goods_id')[0]['goods_id_id']
					sn=Goods.objects.filter(goods_id=gid)[0]
					print('物@料'+sn.goods_station)
					#存入小车下一个目的地
					Car.objects.filter(car_number=num).update(distination=sn.goods_station)
					return HttpResponse(sn.goods_station)

			
			
			if Car.objects.filter(car_number=num,car_state='2'):
				order=OrderPcb.objects.filter(car_number=num,order_state='未完成').order_by('id')[0]
				#两个以上的物料点
				if order.orderpcb_de_set.all().count()>1:
					sta=State.objects.all().get(sta_number='1')
					c=Car.objects.get(car_number=num)
					c.car_state=sta
					c.save()
					orsn=order.orderpcb_de_set.all().values().order_by('goods_id')[0]['order_sn_id']
					#查询未完成的物料点
					if OrderPcb_de.objects.filter(order_sn=orsn,order_state='0'):
						#物料站点号
						gid=order.orderpcb_de_set.filter(order_state='0').values().order_by('goods_id')[0]['goods_id_id']
						sn=Goods.objects.filter(goods_id=gid)[0]
						print('物x料'+sn.goods_station)
						#存入小车下一个目的地
						Car.objects.filter(car_number=num).update(distination=sn.goods_station)
						return HttpResponse(sn.goods_station)
				#状态改为3
				sta=State.objects.all().get(sta_number='3')
				c=Car.objects.get(car_number=num)
				c.car_state=sta
				c.save()
				#先判断是哪个工作类型
				if OrderPcb.objects.get(order_state="未完成",car_number=num).work_type=='1':
					#物料站点号
					print('再X去完成品地点0x03')
					#存入小车下一个目的地
					Car.objects.filter(car_number=num).update(distination='0x03')
					return HttpResponse('0x03')
				else:
					#站点号
					line_number=order.line_id#线体号
					zd=Linebody.objects.filter(line_id=line_number)[0]
					print('站x点'+zd.station_number)
					#存入小车下一个目的地
					Car.objects.filter(car_number=num).update(distination=zd.station_number)
					return HttpResponse(zd.station_number)


		#分配任务
		elif OrderPcb.objects.filter(order_state="未完成",car_number=None):
			order=OrderPcb.objects.filter(order_state="未完成",car_number=None).order_by('id')[0]
			#判断小车停的前后位置
			car=Car.objects.all().get(car_number=num)
			order.car_number=car
			order.save()
			print('create ok')
			#状态改为1
			sta=State.objects.all().get(sta_number='1')
			c=Car.objects.get(car_number=num)
			c.car_state=sta
			c.save()
			#判断订单的工作类型，0表示送料，1表示送完成品
			if OrderPcb.objects.get(order_state="未完成",car_number=num).work_type=='1':
				#先去站点号
				line_number=order.line_id#线体号
				zd=Linebody.objects.filter(line_id=line_number)[0]

				print('先去站点'+zd.station_number)
				#存入小车下一个目的地
				Car.objects.filter(car_number=num).update(distination=zd.station_number)
				return HttpResponse(zd.station_number)
			else:
				#物料站点号
				gid=order.orderpcb_de_set.all().values().order_by('goods_id')[0]['goods_id_id']
				sn=Goods.objects.filter(goods_id=gid)[0]
				print('物料'+sn.goods_station)
				# return HttpResponse()
				#存入小车下一个目的地
				Car.objects.filter(car_number=num).update(distination=sn.goods_station)
				return HttpResponse(sn.goods_station)
				# if Car.objects.filter(car_number=num,car_state='5'):
				# 	if sn.goods_station=='0x01':
				# 		sta=State.objects.all().get(sta_number='3')
				# 		c=Car.objects.get(car_number=num)
				# 		c.car_state=sta
				# 		c.save()
				# 		o=OrderPcb.objects.get(car_number=num,order_state="未完成")
				# 		if OrderPcb.objects.filter(down_time=''):
				# 			o.down_time=tm
				# 		o.save()
				# 		line_number=order.line_id#线体号
				# 		zd=Linebody.objects.filter(line_id=line_number)[0]
				# 		print('由于在取料点1所以去站@点'+zd.station_number)
				# 		return HttpResponse(zd.station_number)

				
		elif Car.objects.filter(car_number=num,car_state='4'):
			sta=State.objects.all().get(sta_number='5')
			c=Car.objects.get(car_number=num)
			c.car_state=sta
			c.save()
			print('没有订单返回0x01，状态改为5',c.default_mark)
			#存入小车下一个目的地
			Car.objects.filter(car_number=num).update(distination=c.default_mark)
			return HttpResponse(c.default_mark)
		elif Car.objects.filter(car_number=num,car_state='5'):
			
			
			print('no order')
			return HttpResponse('')
		else:
			sta=State.objects.all().get(sta_number='5')
			c=Car.objects.get(car_number=num)
			c.car_state=sta
			c.save()
			print('默认回到0x01',c.default_mark)
			#存入小车下一个目的地
			Car.objects.filter(car_number=num).update(distination=c.default_mark)
			return HttpResponse(c.default_mark)



	elif int(state)==2:
		#只要在中途判断有没有小车状态为0的。
		# if Car.objects.filter(car_number=num,car_state='4'):
		# 	if OrderPcb.objects.filter(order_state="未完成",car_number=None):

		return HttpResponse('')



	elif int(state)==4:
		#完成送料
		if Car.objects.filter(car_number=num,car_state='3'):
			o=OrderPcb.objects.get(car_number=num,order_state="未完成")
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

			# #上一个状态置零
			# c=Car.objects.get(car_number=num)
			# Mark.objects.filter(mark_id=c.car_mark).update(mark_state='0')
			# #把现在的点导进去
			# lsta=Linebody.objects.get(line_id=o.line_id)
			# mark=Mark.objects.get(mark_id=lsta.station_number)
			# mark.mark_state='1'
			# mark.save()
			# Car.objects.filter(car_number=num).update(car_mark=mark)


			#站位号
			sta=State.objects.all().get(sta_number='4')
			c=Car.objects.get(car_number=num)
			c.car_state=sta
			c.save()

			print('送料完成')
			return HttpResponse('')
		elif Car.objects.filter(car_number=num,car_state='1'):
			o=OrderPcb.objects.get(car_number=num,order_state="未完成")
			#两个放料时间
			# if OrderPcb.objects.filter(down_time=''):
			# 	o.down_time=tm
			o.save()
			print('装料')

			# #上一个状态置零
			# c=Car.objects.get(car_number=num)
			# Mark.objects.filter(mark_id=c.car_mark).update(mark_state='0')
			# #把现在的点导进去
			# gid=o.orderpcb_de_set.all().values()[0]['goods_id_id']
			# sn=Goods.objects.filter(goods_id=gid)[0]#order_sn

			# mark=Mark.objects.get(mark_id=sn.goods_station)
			# mark.mark_state='1'
			# mark.save()
			# Car.objects.filter(car_number=num).update(car_mark=mark)
			# print(sn.goods_station)

			#修改物料点完成状态
			orsn=o.orderpcb_de_set.filter(order_state='0').values().order_by('goods_id')[0]['id']
			
			OrderPcb_de.objects.filter(id=orsn,order_state='0').update(order_state='1')

			sta=State.objects.all().get(sta_number='2')
			c=Car.objects.get(car_number=num)
			c.car_state=sta
			c.save()
			return HttpResponse('taking')

		elif Car.objects.filter(car_number=num,car_state='5'):
			#上一个状态置零
			# c=Car.objects.get(car_number=num)
			# Mark.objects.filter(mark_id=c.car_mark).update(mark_state='0')
			# #把现在的点导进去
			# mark=Mark.objects.get(mark_id='0x01')
			# mark.mark_state='1'
			# mark.save()
			# Car.objects.filter(car_number=num).update(car_mark=mark)

			print('到达原点')
			return HttpResponse('')
		else:
			print('状态四错误')
			return HttpResponse('')
	else:
		print('return or send error')
		return HttpResponse('return')

