from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
	#name = models.BooleanField(default=bool)
	#job = models.BooleanField(default=bool)
	name = models.CharField(max_length=200)
	job = models.CharField(max_length=200)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('PostDetailView', kwargs={'pk': self.pk})