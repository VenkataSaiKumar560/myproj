from django.db import models

# Create your models here.
class Register(models.Model):
	Name = models.CharField(max_length=40)
	Email = models.EmailField(unique=True,null=True)
	Phone = models.CharField(unique=True,max_length=10)
	Password = models.CharField(unique=True,max_length=30)
	Address = models.CharField(unique=True,max_length=100)
	DOB = models.CharField(max_length=20)
	Gender = models.CharField(max_length=20)
	def __str__(self):
		return self.Email

class Seeking(models.Model):
	Phone = models.CharField(max_length=10)
	Item = models.CharField(max_length=30)
	Quantity = models.CharField(max_length=10)
	def __str__(self):
		return self.Phone

class Helping(models.Model):
	Hitem = models.CharField(max_length=30)
	Hquantity = models.CharField(max_length=10)

	def __str__(self):
		return self.Hitem
		