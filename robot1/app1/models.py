from django.db import models

# Create your models here.
class Robot_1(models.Model):
	date=models.CharField(max_length=30)
	state=models.CharField(max_length=30)
	# d=models.CharField(max_length=33,default=33)
	def __str__(self):
		return self.date
class Now_time_1(models.Model):
	time=models.CharField(max_length=100)
	def __str__(self):
		return self.time
class Second_1(models.Model):
	sec=models.CharField(max_length=100)
	def __str__(self):
		return self.sec



class Robot_2(models.Model):
	date=models.CharField(max_length=30)
	state=models.CharField(max_length=30)
	# d=models.CharField(max_length=33,default=33)
	def __str__(self):
		return self.date
class Now_time_2(models.Model):
	time=models.CharField(max_length=100)
	def __str__(self):
		return self.time
class Second_2(models.Model):
	sec=models.CharField(max_length=100)
	def __str__(self):
		return self.sec


class Robot_3(models.Model):
	date=models.CharField(max_length=30)
	state=models.CharField(max_length=30)
	# d=models.CharField(max_length=33,default=33)
	def __str__(self):
		return self.date
class Now_time_3(models.Model):
	time=models.CharField(max_length=100)
	def __str__(self):
		return self.time
class Second_3(models.Model):
	sec=models.CharField(max_length=100)
	def __str__(self):
		return self.sec


class Robot_4(models.Model):
	date=models.CharField(max_length=30)
	state=models.CharField(max_length=30)
	# d=models.CharField(max_length=33,default=33)
	def __str__(self):
		return self.date
class Now_time_4(models.Model):
	time=models.CharField(max_length=100)
	def __str__(self):
		return self.time
class Second_4(models.Model):
	sec=models.CharField(max_length=100)
	def __str__(self):
		return self.sec