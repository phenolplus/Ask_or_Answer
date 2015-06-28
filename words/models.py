from django.db import models

# Create your models here.

from django.db import models

class Post(models.Model):
	question = models.CharField(max_length=500)
	answer = models.CharField(max_length=500, blank=True)
	answered = models.BooleanField(default=False)

	time_stamp = models.DateTimeField(auto_now_add=True)
