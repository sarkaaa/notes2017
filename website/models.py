from django.db import models
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateField()
    note = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
