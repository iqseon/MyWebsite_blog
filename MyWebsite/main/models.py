from django.db import models
from pip._internal.vcs import git


class Shoes(models.Model):
    title = models.CharField('Brand', max_length=100)
    shoe = models.CharField('Name shoe', max_length=100)
    image = models.ImageField(upload_to='shoes/', blank=False)

    def __str__(self):
        return self.title


class UserAddress:
    pass


class UserPhoneNumber:
    pass