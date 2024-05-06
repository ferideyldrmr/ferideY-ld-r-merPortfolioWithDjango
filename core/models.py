from django.db import models


# Create your models here.
class GeneralSettings(models.Model):
    name = models.CharField(
        defaulte='',
        max_length=254,
        blank=True,
    )
    description = models.TextField(
        blank=True,
        default='',
        max_length=254,
    )
    parameter = models.CharField(
        blank=True,
        max_length=254,
        default='',
    )
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
    )
