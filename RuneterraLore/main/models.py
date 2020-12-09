from django.db import models

# Create your models here.

class Region(models.Model):
	name = models.CharField(max_length=20)
	image = models.ImageField(null=True, blank=True, upload_to='region_imgs')
	image_bg = models.ImageField(null=True, blank=True, upload_to='region_imgs')
	champions_count = models.PositiveSmallIntegerField(default=0)
	description = models.TextField(null=True, blank=True)


	def __str__(self):
		return self.name

class Champion(models.Model):
	name = models.CharField(max_length=20)
	image = models.ImageField(upload_to='champion_imgs',null=True, blank=True)
	region = models.ManyToManyField('Region')

	introduction = models.TextField(null=True, blank=True)
	bio = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name
