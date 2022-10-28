from django.urls import path
from .import views

urlpatterns = [
    path('',views.customer_home),
    path('myorder',views.customer_myorder),
    
    
]