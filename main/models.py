from django.db import models


class MainBanner(models.Model):
    bg_image = models.ImageField(upload_to='banners/')
    text1 = models.CharField(max_length=250)
    text2 = models.CharField(max_length=250)
    image2 = models.ImageField(upload_to='images/')


class Order(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.name


class Discount(models.Model):
    old_price = models.IntegerField()
    new_price = models.IntegerField()

    @property
    def profit(self):
        return self.old_price - self.new_price


class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class InfoAboutProduct(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='images/')


class AboutCompany(models.Model):
    image = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.title


class Disease(models.Model):
    text = models.CharField(max_length=250)


class DiseaseBanner(models.Model):
    image = models.ImageField(upload_to='images/')
    diseases = models.ManyToManyField(Disease)


class HowToUse(models.Model):
    bg_image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.title


class NumberFact(models.Model):
    number = models.CharField(max_length=10)
    text = models.CharField(max_length=250)


class Info(models.Model):
    logo = models.ImageField(upload_to='logo/')
    info = models.CharField(max_length=250)
    tg = models.URLField()
    fb = models.URLField()
    inst = models.URLField()
    yt = models.URLField()
