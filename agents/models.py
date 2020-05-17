from django.db import models

# Create your models here.
class Agent(models.Model):
	name = models.CharField(max_length=20)
	title= models.CharField(max_length=100)
	image= models.ImageField(upload_to='agents/')

	def __str__(self):
		return self.name