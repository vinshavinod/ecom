from django.shortcuts import render

# Create your views here.

def customer_home(request):
    return render(request,'customer/customer_home.html')

def customer_myorder(request):
    return render(request,'customer/myorder.html')

