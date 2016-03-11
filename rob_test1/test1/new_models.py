from django.db import models

# Create your models here.

#物料
class Material(models.Model):
	mat_number=models.CharField(max_length=40,primary_key=True)#物料号
	mat_name=models.CharField(max_length=40,default='')#物料名称
	mat_type=models.CharField(max_length=40)#物料类型
	mat_count=models.IntegerField(default='')#物料数量
	def __str__(self):
		return self.mat_number


#线体
class Linebody_1(models.Model):
	line_number=models.CharField(max_length=40,primary_key=True)#线体号
	station_number=models.CharField(max_length=40)#站点号
	mat_number=models.CharField(max_length=40)#物料号
	mat_name=models.CharField(max_length=40,default='')#物料名称
	mat_type=models.CharField(max_length=40)#物料类型
	mat_count=models.IntegerField(default='')#物料数量
	def __str__(self):
		return self.line_number
#状态号
class State(models.Model):
	sta_number=models.CharField(max_length=30,primary_key=True)
	sta_name=models.CharField(max_length=30)
	def __str__(self):
		return self.sta_number

#小车
class Car(models.Model):
	car_number=models.CharField(max_length=40,primary_key=True)#名称
	car_state=models.ForeignKey(State)#状态
	# postion=models.CharField(max_length=40,default='')
	def __str__(self):
		return self.car_number

#订单
class Order(models.Model):
	order_number=models.CharField(max_length=40)#订单号
	line_number=models.ForeignKey(Linebody)#线体号
	order_time=models.CharField(max_length=40)#创建时间
	order_state=models.CharField(max_length=40,default='未完成')#状态
	car_number=models.ForeignKey(Car,blank=True,null=True)#小车号
	down_time=models.CharField(max_length=50,blank=True)#放物料的时间
	finish_time=models.CharField(max_length=40,default='',blank=True)#完成时间
	def __str__(self):
		return self.order_number



