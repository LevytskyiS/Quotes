import time

from django.db import models
from django.urls import reverse


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Quote(models.Model):
    author = models.ForeignKey(Author, related_name="quotes", on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        # main:quote_detail - name from urls.py
        # main - так как у меня есть имя приложения в urls.py
        return reverse("main:quote_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.text
