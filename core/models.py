from django.db import models

# Create your models here.
class GeneralSetting(models.Model):
    name = models.CharField(
        default="", 
        max_length=254, 
        blank=True
    )
    description = models.TextField(
        default="", 
        max_length=254,
        blank=True
    )
    parameter = models.CharField(
        default="", 
        max_length=254,
        blank=True
    )
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ['name']


class ImageSetting(models.Model):
    name = models.CharField(
        default="", 
        max_length=254, 
        blank=True
    )
    description = models.TextField(
        default="", 
        max_length=254,
        blank=True
    )
    file = models.ImageField(
        default="",
        verbose_name='Image',
        upload_to='images/',
        blank=True
    )
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ['name']