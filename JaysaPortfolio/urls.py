from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path("", views.home, name = 'home'),
   path("about/", views.about, name = 'about'),
   path("portfolio/", views.portfolio, name = 'portfolio'),
   path("contacts", views.contacts, name = 'contacts')  
]