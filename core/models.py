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
        ordering = ['order']


class Experience(AbstractModel):
    company_name = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Company Name',
    )
    job_title = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Job Title',
    )
    job_location = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Job Location',
    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        default=None,
        verbose_name='End Date',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ['start_date']



class Education(AbstractModel):
    school_name = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='School Name',
    )
    major = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Major',
    )
    department = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Department',
    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        default=None,
        verbose_name='End Date',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.school_name
    
    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ['start_date']


class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Social Media Order',
    )
    link = models.URLField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Link',
    )
    icon = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Icon',
    )

    def __str__(self):
        return self.link
    
    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Medias'
        ordering = ['link']


class Document(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Document Order',
    )
    slug = models.SlugField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Slug',
    )
    name = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Document Name',
    )
    button_text = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Button Text',
    )
    file = models.FileField(
        default="",
        verbose_name='File',
        upload_to='documents/',
        blank=True,
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ['order']

