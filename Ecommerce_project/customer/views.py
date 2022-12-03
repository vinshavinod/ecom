from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request,'customer/customer_home.html')

def customer_login(request):
    return render(request,'customer/login.html')

def customer_myorder(request):
    return render(request,'customer/myorder.html')

def customer_mywishlist(request):
    return render(request,'customer/my_wishlist.html')

def customer_category(request):
    return render(request,'customer/category.html')

def modal(request):
    return render(request,'customer/login_modal.html')

def login1(request):
    return render(request,'customer/login1.html')

def signup(request):
    return render(request,'customer/signup.html')

def product_details(request):
    return render(request,'customer/product_details.html')

def customer_my_account(request):
    return render(request,'customer/my_account.html')
