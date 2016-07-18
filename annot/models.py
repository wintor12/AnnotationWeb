from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Story(models.Model):
	name = models.CharField(max_length=100)
	content = models.TextField()
	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Class(models.Model):
	name = models.CharField(max_length=500)
	color = models.CharField(max_length=50, default='#ff0000')
	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Subclass(models.Model):
	name = models.CharField(max_length=500)
	topclass = models.ForeignKey(Class, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
	

@python_2_unicode_compatible
class Label(models.Model):
	name = models.CharField(max_length=500)
	subclass = models.ForeignKey(Subclass, on_delete=models.CASCADE)
	topclass = models.ForeignKey(Class, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Annotator(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	def __str__(self):
		return self.username


@python_2_unicode_compatible
class Annotation(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    annotator = models.ForeignKey(Annotator, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    sentences = models.TextField()
    start = models.IntegerField()
    end = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
		return str(self.time)

@python_2_unicode_compatible
class Complete(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    annotator = models.ForeignKey(Annotator, on_delete=models.CASCADE)
    time = models.DateTimeField()
    def __str__(self):
		return str(self.pk)








