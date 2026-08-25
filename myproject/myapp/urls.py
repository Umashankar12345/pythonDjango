from django.urls import path
from .import views

urlpatterns = [
    path('' , views.home),
    path('contact/' , views.contact),
    path('gallery/' , views.gallery),
    path('about/' , views.about),
    path("receipe/", views.receipe),
    path("resturant/" , views.resturant),
    path("addition/" , views.addition),
    path("multply/" , views.multply),
    path("products/" , views.products),
]