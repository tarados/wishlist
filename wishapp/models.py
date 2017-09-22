from django.db import models
from django.contrib import admin

class Dreamer(models.Model):
    class Meta():
        db_table = 'dreamer'

    dreamer_name = models.CharField(max_length=40)

class Desire(models.Model):
    class Meta():
        db_table = 'desire'

    desire_text = models.TextField()
    desire_date = models.DateTimeField()
    desire_dreamer = models.ForeignKey(Dreamer)


