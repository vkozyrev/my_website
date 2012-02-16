from django.db import models

class Application(models.Model):

    applicationName = models.CharField(verbose_name = 'Application Name', max_length = 100)
    applicationImage = models.ImageField(verbose_name = 'Application Icon', upload_to = 'img/', null = True, blank = True)
    applicationDescription = models.CharField(verbose_name = 'Application Description', max_length = 2000)
    iTunesLink = models.URLField(verbose_name = 'iTunes Link');
    supportEmail = models.EmailField(verbose_name = 'Support Email', max_length = 100)

# Create your models here.
