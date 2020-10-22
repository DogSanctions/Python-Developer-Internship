from django.db import models
from datetime import datetime, date
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    username = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.username


class Pet(models.Model):
    pet_name = models.CharField(max_length=50, blank=False, null=False)
    pet_age = models.IntegerField(blank=False, null=False)
    pet_type = models.CharField(max_length=50, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.pet_type


class Post(models.Model):
    park_name = models.CharField(max_length=50, blank=False, null=False)
    park_location = models.CharField(max_length=100, blank=False, null=False)
    park_review = models.CharField(max_length=150, blank=False, null=False)
    park_thumbs = models.BooleanField(default=True)
    date_visited = models.DateField(default=date.today)
    post_time = models.TimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=False, null=False)

    Posts = models.Manager()

    def __str__(self):
        return self.park_name

    class Meta:
        ordering = ['park_name']
