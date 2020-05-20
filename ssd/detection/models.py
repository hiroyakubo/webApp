from django.db import models
from django.conf import settings
from django.utils import timezone


def get_detection_image_path(instance, filename):
    return "images/detection/{}".format(filename)
    
class Image(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to=get_detection_image_path, verbose_name="推論用画像を選択", null=True)

    @property
    def picture_path(self):
        return str(self.picture)