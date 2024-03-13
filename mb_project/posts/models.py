from django.test import TestCase

from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):

    text = models.TextField()

    def __str__(self):
        """Строковое отображение модели"""
        return self.text[:50]


