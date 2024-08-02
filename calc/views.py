from django.shortcuts import render 
from .models import *
def home(request):
    return render(request,'home.html',{'name':'Raju'})
def add(request):
    val1=int(request.POST["num1"])
    val2=int(request.POST["num2"])
    val3=val1+val2
    return render(request, "result.html",{"result":val3})
def dashboard(request): 
    return render(request,'dashboard.html')
def dashboard(request):
    customers=Customer.objects.all()
    return render(request,"dashboard.html",{"customers":customers})
def products(request):
    products= Product.objects.all() 
    return render(request ,'products.html',{'products':products})