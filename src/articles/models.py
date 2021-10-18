from django.db import models


class FutureModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    # img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class FutureImage(models.Model):
    # future = models.ManyToManyField('FutureModel')
    imglist = models.ImageField(upload_to='images')


class ServiceModel(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=450)

    def __str__(self):
        return self.title


class TeamModel(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=50)
    twitter = models.CharField(max_length=70, blank=True)
    facebook = models.CharField(max_length=70, blank=True)
    instagram = models.CharField(max_length=70, blank=True)
    telegram = models.CharField(max_length=70, blank=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    types = models.CharField(max_length=50)

    def __str__(self):
        return self.types


class ImagePortfolio(models.Model):
    portfolio = models.ManyToManyField("Portfolio")
    image = models.ImageField(upload_to='images')
