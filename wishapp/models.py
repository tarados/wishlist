import os
import requests
from django.conf import settings
from django.db import models
from django.core.files import File
from django.contrib.auth.models import User


class Desirelist(models.Model):
    class Meta:
        db_table = 'desirelist'

    desirelist_name = models.TextField()
    desirelist_user = models.ForeignKey(User, on_delete=models.CASCADE)
    desirelist_substitute_id = models.CharField(max_length=8, default='', unique=True)



class Desire(models.Model):
    class Meta:
        db_table = 'desire'

    desire_text = models.TextField()
    desire_date = models.DateTimeField()
    desire_user = models.ForeignKey(User, on_delete=models.CASCADE)
    desire_order_user = models.ForeignKey(User, related_name='order', null=True, on_delete=models.CASCADE)
    desire_state = models.IntegerField(default=0)
    desire_order = models.IntegerField(default=0)
    desire_img = models.TextField(null=True)
    desire_title = models.CharField(null=True, max_length=250)
    desire_photo = models.ImageField(upload_to='uploads', null=True, blank=True)
    desire_desirelist = models.ForeignKey(Desirelist, models.SET_NULL, blank=True, null=True,)
    desire_substitute_id = models.CharField(max_length=8, default='', unique=True)

    def fetch_remote_img(self, url):
        result = requests.get(url)
        file_name = 'icon_{0}.{1}'.format(self.id, url.split('.')[-1])
        path_file = os.path.join(settings.MEDIA_ROOT, file_name)
        out = open(path_file, "wb")
        out.write(result.content)
        out.close()
        self.desire_photo.save(file_name, File(open(path_file, 'rb')))
        self.save()
        os.remove(path_file)

    def determine_height_img(self):
        h = Desire.objects.get(id=self.id).desire_photo.height
        w = Desire.objects.get(id=self.id).desire_photo.width
        image_factor = h / w
        return image_factor

