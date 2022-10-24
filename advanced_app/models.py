from tkinter import CASCADE
from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length = 256)
    principle = models.CharField(max_length = 256)
    location = models.CharField(max_length = 256)

    def __str__(self) -> str:
        return self.name
    def get_absolute_url(self) -> str:
        return reverse('advanced_app:detail',kwargs={'pk':self.pk})


class Students(models.Model):
    name = models.CharField(max_length = 256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students', on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.name