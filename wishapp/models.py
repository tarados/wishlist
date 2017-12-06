from django.db import models
from django.contrib.auth.models import User

class Desire(models.Model):
    class Meta():
        db_table = 'desire'

    desire_text = models.TextField()
    desire_date = models.DateTimeField()
    desire_user = models.ForeignKey(User)
    desire_order_user = models.ForeignKey(User, related_name='order', null=True)
    desire_state = models.IntegerField(default=0)
    desire_order = models.IntegerField(default=0)
    desire_img = models.TextField(null=True)


