from django.db import models
from django.urls import reverse

# Create your models here.
class Widget(models.Model):
    widget = models.CharField(max_length=50)

    def __str__(self):
        return self.widget

    def get_absolute_url(self):
        return reverse('index')
