from django.db import models


# Create your models here.
class BlogTopic(models.Model):
	title = models.CharField(max_length=32, unique=True)
	slug = models.SlugField()


class Blog(models.Model):
	title = models.CharField(max_length=32)
	topic = models.ForeignKey(BlogTopic, on_delete=models.CASCADE)
