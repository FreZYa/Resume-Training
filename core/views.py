from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from core.models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialMedia, Document


def _setting(name, default=''):
    setting = GeneralSetting.objects.filter(name=name).first()
    return setting.parameter if setting else default


def _image(name):
    image = ImageSetting.objects.filter(name=name).first()
    return image.file if image else None


def layout(request):
    # Settings are edited in the admin panel; a fresh database has none yet,
    # so fall back to empty values instead of raising DoesNotExist.
    documents = Document.objects.all().order_by('order')
    site_title = _setting('site_title')
    site_keywords = _setting('site_keywords')
    site_description = _setting('site_description')
    home_banner_name = _setting('home_banner_name')
    home_banner_title = _setting('home_banner_title')
    home_banner_description = _setting('home_banner_description')
    about_myself_welcome = _setting('about_myself_welcome')
    about_myself_footer = _setting('about_myself_footer')
    header_logo = _image('header_logo')
    home_banner_image = _image('home_banner_image')
    site_favicon = _image('site_favicon')

    skills = Skill.objects.all().order_by('order')
    social_medias = SocialMedia.objects.all().order_by('order')
    context = {
        'documents': documents,
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer': about_myself_footer,
        'header_logo': header_logo,
        'home_banner_image': home_banner_image,
        'site_favicon': site_favicon,
        'skills': skills,
        'social_medias': social_medias,
    }
    return context

# Create your views here.
def home(request):

    experiences = Experience.objects.all().order_by('start_date')
    educations = Education.objects.all().order_by('start_date')

    context = {
        'experiences': experiences,
        'educations': educations,
    }
    return render(request, 'index.html', context)


def redirect_urls(request, slug):
    document = get_object_or_404(Document, slug=slug)
    if document.file and document.file.url:
        return redirect(document.file.url)
    else:
        return redirect('home')