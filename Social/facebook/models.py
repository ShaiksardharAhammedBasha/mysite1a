from django.db import models

# Create your models here.

class Profile(models.Model):

	username = models.CharField(max_length = 250)
	email    = models.EmailField()
	password = models.CharField(max_length = 200)
	posts    = models.CharField(max_length = 200)

	friend_list = models.CharField(max_length = 25)

	def __str__(self):

		return self.username