from django.db import models
from django.contrib.auth.models import User

class Secret(models.Model):
    idEmail = models.ForeignKey(User, on_delete=models.CASCADE, related_name="relate")
    website = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    notes = models.CharField(max_length=300)
    build_date = models.DateTimeField('date built')
    def __str__(self):
        return self.name
