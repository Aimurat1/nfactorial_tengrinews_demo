from django.db import models

# Create your models here.

class NewsInstance(models.Model):
    title = models.CharField(max_length=255)
    annotation = models.TextField(null=True)
    content = models.TextField()
    datetime = models.DateTimeField()

    image_url = models.CharField(max_length=255)
    url = models.CharField(max_length=255)


class NewsTag(models.Model):

    news = models.ForeignKey(NewsInstance, on_delete=models.CASCADE, related_name="tags")
    tag = models.CharField(max_length=255)
    

