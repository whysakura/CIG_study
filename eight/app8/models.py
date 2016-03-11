from django.db import models

# Create your models here.
class Order(models.Model):#执行的命令
	name=models.CharField(max_length=33)
	order=models.IntegerField(default='')
	def __str__(self): 
		nam=str(name)
		return self.name
class Data_1(models.Model):#存储数据
	date=models.CharField(max_length=30)
	state=models.CharField(max_length=30)
	robot=models.IntegerField(default=1)
	def __str__(self):
		return self.date
class Data_2(models.Model):
	date=models.CharField(max_length=30)
	state=models.CharField(max_length=30)
	robot=models.IntegerField(default=2)
	def __str__(self):
		return self.date
class Data_3(models.Model):
	date=models.CharField(max_length=30)
	state=models.CharField(max_length=30)
	robot=models.IntegerField(default=3)
	def __str__(self):
		return self.date
class Data_4(models.Model):
	date=models.CharField(max_length=30)
	state=models.CharField(max_length=30)
	robot=models.IntegerField(default=4)
	def __str__(self):
		return self.date