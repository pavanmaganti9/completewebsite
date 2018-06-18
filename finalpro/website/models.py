from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import pymongo


# Create your models here.
class website(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.title
	class Meta:
		verbose_name_plural ="Contents"
		
class FormData(models.Model):
	name = models.CharField(max_length=20)
	email = models.CharField(max_length=30)
	address = models.TextField()
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural ="FormData"
		
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
	# def __str__(self):
		# return self.description
	# class Meta:
		# verbose_name_plural ="Documents"