from django.db import models


class DownloadFile(models.Model):
    file = models.FileField('media/data.json')

    def __str__(self):
        return self.file.url
