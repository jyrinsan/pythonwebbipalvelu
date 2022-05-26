from django.db import models

class Entry(models.Model):
	trainer = models.CharField(max_length=300)
	description = models.TextField()
	date = models.DateField();
	duration = models.DurationField()
	exercise = models.ForeignKey(
		'Exercise',
		on_delete=models.CASCADE
	)

	def __str__(self):
		return f"{self.trainer}, {self.exercise.name}, {self.duration}"

	def get_absolute_url(self):
		return f"/entries/{self.pk}"

class Exercise(models.Model):
	name = models.CharField(max_length=300)

	def __str__(self):
		return self.name
