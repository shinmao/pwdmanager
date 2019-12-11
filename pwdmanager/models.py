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
        return self.website
    def get_site(self):
        return self.website
    def get_username(self):
        return self.username
    def get_email(self):
        return self.email
    def get_password(self):
        return self.password
    def get_notes(self):
        return self.notes
    def get_build_date(self):
        return self.build_date
