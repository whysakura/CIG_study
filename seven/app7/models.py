from django.db import models
from app4.models import *
# Create your models here.
class Author(models.Model):
	name=models.CharField(max_length=30)
	city=models.CharField(max_length=20)
	email=models.EmailField()
	def __str__(self):
		return self.name
class Publisher(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=60)
	city=models.CharField(max_length=30)
	province=models.CharField(max_length=30)
	country=models.CharField(max_length=30)
	url=models.URLField()
	def __str__(self):
		return self.name
class Book(models.Model):
	authors=models.ManyToManyField(Author)
	publishers=models.ForeignKey(Publisher)
	date=models.DateField()
	name=models.CharField(max_length=30)
	shuzi=models.IntegerField(default=0)
	def __str__(self):
		return self.name
class Person(models.Model):
	Name=(('a','achar'),('s','sakura'),('l','love'),)
	name=models.CharField(max_length=100,choices=Name)
	num=models.IntegerField(default='')
class Test(models.Model):
	wife=models.CharField(max_length=20)
	say=models.CharField('这是我说的',max_length=22)
	person=models.ForeignKey(Question,default='')
	def __str__(self):
		return self.wife