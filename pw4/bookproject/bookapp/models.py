from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=300)
	author = models.CharField(max_length=300)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return f"/books/{self.pk}"
