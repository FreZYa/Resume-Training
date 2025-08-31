from django.db import models

# Create your models here.
class GeneralSettings(models.Model):
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
    
    
