from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug>/', views.redirect_urls, name='redirect_urls'),
]   