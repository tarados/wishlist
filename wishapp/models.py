from django.db import models
from django.contrib import admin

class Wishmakers(models.Model):
    user = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    description = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.user

admin.site.register(Wishmakers)