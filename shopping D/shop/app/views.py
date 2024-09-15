from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Cart, OrderPlaced
from.forms import CustomeRegistrationFrom
from django.contrib import messages
# def home(request):
#  return render(request, 'app/home.html')

# i am crea te this view>
class productViws(View):
 def get(self, request):

  bottomwears = Product.objects.filter(category='BW')
  topwears = Product.objects.filter(category='TW')
  mobiles = Product.objects.filter(category='M')
  laptop = Product.objects.filter(category='L')

  return render(request,'app/home.html',
   {'topwear':topwears, 'bottomwears':bottomwears, 'mobiles':mobiles,'laptop':laptop} )


# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
 def get(self,request,pk):
  product = Product.objects.get(pk=pk)
  return render(request,'app/productdetail.html' ,
   {'product':product})
  



def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
 if data == None:
  mobiles = Product.objects.filter(category='M').filter(brand=data)
 elif data == 'redami' or data ==  'poco':
  mobiles = Product.objects.filter(category='M').filter(brand=data)
 return render(request, 'app/mobile.html', {'mobiles':mobiles})

# def login(request):
#  return render(request, 'app/login.html')
# # 
# this is register form 
class CustomerRegistrationView(View):
 def get(self, request,):
  form = CustomeRegistrationFrom()
  return render (request, 'app/customerregistration.html',
   {'form':form})
 
 def post(self,request):
  form = CustomeRegistrationFrom(request.POST)
  if form.is_valid():
   messages.success(request,'Congratulations!! registered Successfully.')
   form.save()
#    return redirect('login')
#   else:

  return render(request, 'app/customerregistration.html',
   {'form':form})



def checkout(request):
 return render(request, 'app/checkout.html')

# this ios loptop
# def laptop(request, data=None):
#  if data == None:
#   laptop = Product.objects.filter(category='L').filter(brand=data)
#  elif data == 'dell' or data ==  'hp':
#   laptop = Product.objects.filter(category='L').filter(brand=data)
#  return render(request, 'app/laptop.html', {'laptop':laptop})