from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employer(models.Model):
	name		= models.CharField(max_length=50)
	loc			= models.CharField(max_length=50)
	business	= models.CharField(max_length=50, blank=True)
	
	def __unicode__(self):
		return self.name


class Author(models.Model):
	user		= models.OneToOneField(User)
	address		= models.TextField(blank=True)
	birthday	= models.DateField(blank=True)
	email2		= models.EmailField(blank=True)
	phone		= models.CharField(max_length=20, blank=True)
	
	def __unicode__(self):
		return self.user.first_name

	
class Job(models.Model):
	position	= models.CharField(max_length=30)
	author		= models.ForeignKey(Author)
	employer	= models.ForeignKey(Employer)
	descr		= models.TextField()
	start_date	= models.DateField()
	end_date	= models.DateField()
	
	def __unicode__(self):
		return self.position


class CV(models.Model):
	author	= models.ForeignKey(Author)
	descr	= models.TextField(blank=True)
	added	= models.DateTimeField(auto_now_add=True)
	updated	= models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.descr



	
	
	