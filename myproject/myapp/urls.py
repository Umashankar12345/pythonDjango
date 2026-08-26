from django.urls import path, re_path 
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
    re_path(r'^user/(?P<username>[a-zA-Z]+)/$', views.user_profile),
]