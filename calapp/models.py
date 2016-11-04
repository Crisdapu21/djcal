from django.db import models

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length = 50)
	location = models.CharField(max_length = 100)
	start = models.DateTimeField(blank = False)
	end = models.DateTimeField(blank = False)
	allday = models.BooleanField()
	description = models.TextField(max_length = 200)
	synced = models.BooleanField(default = False)
	gid = models.CharField(default = '',max_length = 100)