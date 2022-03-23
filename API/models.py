from django.db import models
import datetime

# Create your models here.


class News(models.Model): 
    story = models.TextField(blank=False)
    headline = models.CharField(max_length=100)
    writer = models.CharField(max_length=30)
    photographer = models.CharField(max_length=30)
    date_time = models.DateTimeField(default=datetime.datetime.now())
    date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.headline
    