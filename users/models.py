import uuid

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100, unique=False)
    last_name = models.CharField(max_length=100, unique=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def serialize(self) -> dict:
        return {
            "user_id": self.user.id,
            "username": self.user.username,
            "user_email": self.user.email,
        }


class GrappleEntry(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
    hours_trained = models.IntegerField(default=0)
    minutes_trained = models.IntegerField(default=0)
    grappling_type = models.CharField(default="Gi")
    notes = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.user)
