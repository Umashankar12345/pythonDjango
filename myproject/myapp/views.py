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


def addition(request):
    num1 = int(request.GET.get("num1"))
    num2 = int(request.GET.get("num2"))

    result = num1 + num2

    return HttpResponse(f"Result: {result}")

def  multply(request):
    num1 = int(request.GET.get("num1"))
    num2 = int(request.GET.get("num2"))

    result = num1 * num2

    return HttpResponse(f"Result: {result}")

def products(request):
    product_name = request.GET.get("product_name")
    product_price = request.GET.get("product_price")
    product_quantity = request.GET.get("product_quantity")

    return  HttpResponse(f"product_name:{product_name} , product_price:{product_price} , product_quantity:{product_quantity}")

# //calculation of addition and multiplication is done using GET method. The values are passed in the URL as query parameters. For example, to add two numbers, you can use the following URL: http://localhost:8000/addition/?num1=5&num2=10. Similarly, to multiply two numbers, you can use the following URL: http://localhost:8000/multply/?num1=5&num2=10.



# //regular expressions

def user_profile(request , username):
    return  HttpResponse(f"userProfile: {username}")
