from django.db import models
from django.contrib import admin

class User(models.Model):
    first_name = models.CharField(max_length=30)
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Wishmaker(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=40)
    description = models.TextField()
    publication_date = models.DateField()

    def __unicode__(self):
        return u'%s %s' % (self.user, self.publication_date)

admin.site.register(Wishmaker)