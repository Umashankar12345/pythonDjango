from django.http import HttpResponse

def home(request):
    return HttpResponse("My Home Page")

def contact(request):
    return HttpResponse("My Contact Details")

def gallery(request):
    return HttpResponse("My Gallery Photos")

def about(request):
    return HttpResponse("About Us")