from django.db import models

class Dreamer(models.Model):
    class Meta():
        db_table = 'dreamer'

    dreamer_name = models.CharField(max_length=40)

class Desire(models.Model):
    class Meta():
        db_table = 'desire'

    desire_text = models.TextField(verbose_name='Desire text')
    desire_dreamer = models.ForeignKey(Dreamer)



