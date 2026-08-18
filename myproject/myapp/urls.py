from django.urls import path
from .import views

urlpatterns = [
    path('' , views.home),
    path('contact/' , views.contact),
    path('gallery/' , views.gallery),
    path('about/' , views.about),
]