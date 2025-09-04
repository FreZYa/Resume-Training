from django.urls import path
from . import views

urlpatterns = [
    path('contact_form/', views.contact_form, name='contact_form'),
    path('contact/', views.contact, name='contact'),
]