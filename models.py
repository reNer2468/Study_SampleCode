from django.db import models

# Create your models here.
class Analize_Data(models.Model):
    PublishedAt  =models.DateTimeField()
    Title        =models.TextField()
    URL          =models.URLField()
    Duration     =models.DurationField()
    ViewCount    =models.PositiveIntegerField()
    EmbedHtml    =models.TextField()
    NumChats     =models.TextField(null=True)
    ChatCount    =models.PositiveIntegerField()
    ChatRate     =models.FloatField()
    MedianRate   =models.FloatField()
    StdRate      =models.FloatField()
    MaxRate      =models.FloatField()
