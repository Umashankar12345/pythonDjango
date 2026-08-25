from django.http import HttpResponse

def home(request):
    return HttpResponse("My Home Page")

def contact(request):
    return HttpResponse("My Contact Details")

def gallery(request):
    return HttpResponse("My Gallery Photos")

def about(request):
  return HttpResponse("About Us")

def receipe(request):
    food = request.GET.get("food")
    return HttpResponse(food)


def  resturant(request):
    food = request.GET.get("food")
    city = request.GET.get("city")
    rating = request.GET.get("rating")
    return HttpResponse(f"Food: {food}, City: {city}, Rating: {rating}")