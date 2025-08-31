from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True
    )

    class Meta:
        abstract = True
        ordering = ['updated_date']

# Create your models here.
class GeneralSetting(AbstractModel):
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

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ['name']


class ImageSetting(AbstractModel):
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

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ['name']

    
class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Skill Order',
    )
    name = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Skill Name',
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Skill Percentage',
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'