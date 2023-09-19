# from django.shortcuts import render
# from django.http import HttpResponse

# def members(request):
#     return HttpResponse("Yes!")


from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import ProductCategory, Users



x = ''

@api_view(['GET'])
def routes(request):
  allRoutes = [
    {
      'Endpoint': '/login/',
      'method': 'GET',
      'body': None,
      'description': "Returns a user"
    }
  ]
  return Response(allRoutes)



def jameel(request):
  return render(request, 'jameel.html')


def products(request):
  products_category_list = ProductCategory.objects.all().values()
  template = loader.get_template('products.html')
  context = {
    'product_category_list' : products_category_list
  }
  return HttpResponse(template.render(context, request))


def signup(request):
  
  if request.method == "POST":
    
    usernameinput = request.POST['usernamefield']
    passwordinput = request.POST['passwordfield']

    user = Users(username=usernameinput, password=passwordinput)
    user.save()
    
    return redirect('prod/')

  return render(request, 'signup.html')



def login(request):
  
  if request.method == "POST":
    
    usernameinput = request.POST['usernamefield']
    passwordinput = request.POST['passwordfield']

    user = Users.objects.filter(username=usernameinput, password=passwordinput).values()


    if user.count() > 0:
      global x 
      x = user
      return redirect('/profile')
    else:
      print("Wop")

  return render(request, 'login.html')


def profile(request):
 
    context = {
      'current_user' : x
    }

    return render(request, 'profile.html', context)

