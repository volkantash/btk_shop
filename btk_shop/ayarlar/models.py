from django.db import models

# Ayarlar

class Uygulamalar(models.Model):
    ad = models.CharField(max_length=200)

class Url(models.Model):
    url = models.SlugField()
    uyg = models.CharField(max_length=200, default="uyg")

    def __str__(self):
        return self.url