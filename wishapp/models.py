from django.db import models
from django.contrib.auth.models import User

class Desire(models.Model):
    class Meta():
        db_table = 'desire'

    desire_text = models.TextField()
    desire_date = models.DateTimeField()
    desire_user = models.ForeignKey(User)



