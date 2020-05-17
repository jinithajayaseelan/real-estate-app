from django.db import models

property_type = [
	('sale', "sale"),
	('rent', "rent")
]

#about the property
class Property(models.Model):
	name= models.CharField(max_length=50)
	description= models.CharField(max_length=100)
	property_type = models.CharField(choices= property_type, max_length=10)
	price= models.PositiveIntegerField()
	category= models.ForeignKey('Category', null=True, on_delete= models.SET_NULL)
	area= models.DecimalField(decimal_places=2, max_digits=10)
	beds_number= models.PositiveIntegerField()
	baths_number= models.PositiveIntegerField()
	garages_number= models.PositiveIntegerField()
	image= models.ImageField(upload_to= 'property/', null=True)
	location = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.name

class Category(models.Model):
	category_name = models.CharField(max_length=30)
	image= models.ImageField(upload_to= 'category/', null=True)

	def __str__(self):
		return self.category_name		

#this is for forms	
class Reserve(models.Model):
	name= models.CharField(max_length=50)
	email= models.EmailField()
	notes= models.TextField()
	def __str__(self):
		return self.name