from django.db import models
from django.db.models.base import Model
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.
class Snack(models.Model):
    title = models.CharField(max_length=60)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=265)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("snack_detail", args=[str(self.id)])

class Drinks(models.Model):
    title = models.CharField(max_length=60)
    purchaser = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    description = models.TextField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("snack_detail", args=[str(self.id)])