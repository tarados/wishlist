from django.db import models
from django.contrib import admin

class Wishmaker(models.Model):
    user = models.CharField(max_length=40)
    description = models.TextField()
    publication_date = models.DateField()

    def __unicode__(self):
        return u'%s %s' % (self.user, self.publication_date)

admin.site.register(Wishmaker)