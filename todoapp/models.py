from django.db import models

# Create your models here.
class Task(models.Model):
	task_head = models.CharField(max_length=255)
	description = models.TextField()

	def __str__(self):
		return str(self.task_head)

