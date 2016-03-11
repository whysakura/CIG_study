from django.db import models

# Create your models here.
class Question(models.Model):
	question=models.CharField(max_length=200)
	date=models.DateTimeField()
	def __str__(self):
		return self.question
class Choice(models.Model):
	question=models.ForeignKey(Question)
	choice=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	def __str__(self):
		return self.choice