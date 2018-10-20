from django.db import models
from django.contrib.auth.models import User

# User Models
class Article(models.Model):
	owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	description = models.TextField()
	img = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

class Profile(models.Model):
	CHOICES = ((False, 'Not verified'),(True, 'Verified'))
	owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	description = models.TextField()
	img = models.ImageField(null=True, blank=True)
	points = models.IntegerField()
	verified = models.BooleanField(choices = CHOICES, default =0)
	def __str__(self):
		return self.name

class Hazerd(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	img = models.ImageField(null=True, blank=True)
	LOW = 'l'
	MEDIUM = 'm'
	HIGH = 'h'
	CHOICES = (
		(LOW, 'low'),
		(MEDIUM, 'medium'),
		(HIGH, 'high'),
	)
	danger_level = models.CharField(
		max_length=1,
		choices=CHOICES,
		default=LOW,
	)
	def __str__(self):
		return self.name

class Quest(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	img = models.ImageField(null=True, blank=True)
	stats1 = models.ImageField(null=True, blank=True)
	stats2 = models.ImageField(null=True, blank=True)
	stats3 = models.ImageField(null=True, blank=True)

	points = models.IntegerField()
	location = models.CharField(max_length=250)
	LOW = 'l'
	MEDIUM = 'm'
	HIGH = 'h'
	CHOICES = (
		(LOW, 'low'),
		(MEDIUM, 'medium'),
		(HIGH, 'high'),
	)
	level = models.CharField(
		max_length=1,
		choices=CHOICES,
		default=MEDIUM,
	)
	def __str__(self):
		return self.name


class Maped(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	img = models.ImageField(null=True, blank=True)
	location = models.CharField(max_length=250)


	def __str__(self):
		return self.name

class Camp(models.Model):
	name = models.CharField(max_length=120)
	location = models.CharField(max_length=250)
	description = models.TextField()
	img = models.ImageField(null=True, blank=True)
	number = models.DecimalField(max_digits=6, decimal_places=3)

	def __str__(self):
		return self.name

#types of needed materials

class Material(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	img = models.ImageField(null=True, blank=True)


class Task(models.Model):
	CHOICES = ((False, 'not done'),(True,'done'))
	name = models.CharField(max_length=120)
	description = models.TextField()
	img = models.ImageField(null=True, blank=True)
	status = models.BooleanField(choices=CHOICES, default=0) #choices
