from django.db import models

class Camera(models.Model):
	university_name = models.CharField(max_length = 500)
	link = models.CharField(max_length = 1000)
	snap_link = models.CharField(max_length = 1000, blank = True)

	def __str__(self):
		return self.university_name
