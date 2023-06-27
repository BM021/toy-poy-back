from django.db import models

# Create your models here.


class Category(models.Model):
    objects = models.Model
    name_uz = models.CharField(max_length=120, null=True, blank=True)
    name_ru = models.CharField(max_length=120, null=True, blank=True)
    category_photo = models.ImageField(upload_to='media', null=True, blank=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name_ru


class Card(models.Model):
    objects = models.Model
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    card_name_uz = models.CharField(max_length=120, null=True, blank=True)
    card_name_ru = models.CharField(max_length=120, null=True, blank=True)
    card_desc_uz = models.TextField(max_length=250, null=True, blank=True)
    card_desc_ru = models.TextField(max_length=250, null=True, blank=True)
    card_number = models.CharField(max_length=30, null=True, blank=True)
    card_site_link = models.URLField(max_length=120, null=True, blank=True)
    card_telegram_link = models.URLField(max_length=120, null=True, blank=True)
    card_instagram_link = models.URLField(max_length=120, null=True, blank=True)
    is_top = models.BooleanField(default=False)
    count = models.IntegerField(default=0)

    logo = models.ImageField(upload_to='media', null=True, blank=True)
    card_image1 = models.ImageField(upload_to='media', null=True, blank=True)
    card_image2 = models.ImageField(upload_to='media', null=True, blank=True)
    card_image3 = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.card_name_ru


class Star(models.Model):
    objects = models.Model
    name_uz = models.CharField(max_length=60, null=True, blank=True)
    name_ru = models.CharField(max_length=60, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    site_url = models.URLField(null=True, blank=True)
    telegram_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    count = models.IntegerField(default=0)

    star_image1 = models.ImageField(upload_to='media', null=True, blank=True)
    star_image2 = models.ImageField(upload_to='media', null=True, blank=True)
    star_image3 = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name_ru


class Leading(models.Model):
    objects = models.Model
    name_uz = models.CharField(max_length=60, null=True, blank=True)
    name_ru = models.CharField(max_length=60, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    site_url = models.URLField(null=True, blank=True)
    telegram_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    count = models.IntegerField(default=0)

    image1 = models.ImageField(upload_to='media', null=True, blank=True)
    image2 = models.ImageField(upload_to='media', null=True, blank=True)
    image3 = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name_ru


class DutyArtist(models.Model):
    objects = models.Model
    name_uz = models.CharField(max_length=60, null=True, blank=True)
    name_ru = models.CharField(max_length=60, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    site_url = models.URLField(null=True, blank=True)
    telegram_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    count = models.IntegerField(default=0)

    image1 = models.ImageField(upload_to='media', null=True, blank=True)
    image2 = models.ImageField(upload_to='media', null=True, blank=True)
    image3 = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name_ru


class Shop(models.Model):
    objects = models.Model
    name_uz = models.CharField(max_length=60, null=True, blank=True)
    name_ru = models.CharField(max_length=60, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    site_url = models.URLField(null=True, blank=True)
    telegram_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    count = models.IntegerField(default=0)

    image1 = models.ImageField(upload_to='media', null=True, blank=True)
    image2 = models.ImageField(upload_to='media', null=True, blank=True)
    image3 = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name_ru


class Ad(models.Model):
    objects = models.Model
    name_uz = models.CharField(max_length=60, null=True, blank=True)
    name_ru = models.CharField(max_length=60, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    ad_photo = models.ImageField(upload_to='media', null=True, blank=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name_ru


class AdCatalog(models.Model):
    objects = models.Model
    name_uz = models.CharField(max_length=60, null=True, blank=True)
    name_ru = models.CharField(max_length=60, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    ad_photo = models.ImageField(upload_to='media', null=True, blank=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name_ru


class Other(models.Model):
    objects = models.Model
    name_uz = models.CharField(max_length=60, null=True, blank=True)
    name_ru = models.CharField(max_length=60, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    site_url = models.URLField(null=True, blank=True)
    telegram_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    count = models.IntegerField(default=0)

    image1 = models.ImageField(upload_to='media', null=True, blank=True)
    image2 = models.ImageField(upload_to='media', null=True, blank=True)
    image3 = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name_ru
