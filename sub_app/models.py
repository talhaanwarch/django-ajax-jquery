from django.db import models

# Create your models here.
class TextModel(models.Model):
	text=models.CharField(max_length=200)
	file=models.FileField(upload_to='files')