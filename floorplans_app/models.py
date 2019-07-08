from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    address = models.CharField(max_length=100)

    def __repr__(self):
        return '<Project: {}>'.format(self.address)

    def __str__(self):
        return '{}'.format(self.address)
