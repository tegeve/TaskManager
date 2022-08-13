from django.db import models


class Contact(models.Model):
    name = models.CharField('Name', max_length=120)
    city = models.CharField('City',max_length=120)
    county = models.CharField('County',max_length=120)
    street_name = models.CharField('Street Name',max_length=120)
    street_number =models.IntegerField('Street Number')
    floor =models.IntegerField('Floor')
    building_info =models.CharField('Building Info',max_length=120)
    apartment_number =models.IntegerField('Apartment Number')
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('contact Phone', max_length=20, blank=True)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email Address', blank=True)

    def __str__(self):
        return self.name
