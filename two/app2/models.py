from django.db import models

# Create your models here.
class Article(models.Model):
	title=models.CharField(u'标题',max_length=200)
	content=models.TextField(u'内容')
	def __str__(self):
		return self.title