from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import CustomUser
# Create your views here.

def frontpage(request):
    products = [
        {'image': 'images/mobimg1.jpeg', 'title': 'Samsung Ultra', 'price': '70,000 Rs', 'label': 'New'},
        {'image': 'images/mobimg1.jpeg', 'title': 'Samsung Ultra', 'price': '70,000 Rs', 'label': 'Used'},
        {'image': 'images/mobimg1.jpeg', 'title': 'Samsung Ultra', 'price': '70,000 Rs', 'label': 'Used'},
    ]
    
    return render(request, 'home.html', {'products': products})

from django.shortcuts import render

def main_marketplace(request, user_id):
    products = [
        {'id': 1, 'image': 'images/mobimg1.jpeg', 'name': 'Samsung ultra', 'price': '70,000 Rs', 'condition': 'New', 'location': 'Lahore'},
        {'id': 2, 'image': 'images/mobimg1.jpeg', 'name': 'Samsung ultra', 'price': '70,000 Rs', 'condition': 'New', 'location': 'Lahore'},
        {'id': 3, 'image': 'images/mobimg1.jpeg', 'name': 'Samsung ultra', 'price': '70,000 Rs', 'condition': 'Used', 'location': 'Lahore'},
        {'id': 4, 'image': 'images/mobimg1.jpeg', 'name': 'Samsung ultra', 'price': '70,000 Rs', 'condition': 'Used', 'location': 'Lahore'},
        {'id': 5, 'image': 'images/mobimg1.jpeg', 'name': 'Samsung ultra', 'price': '70,000 Rs', 'condition': 'Used', 'location': 'Lahore'},
        {'id': 6, 'image': 'images/mobimg1.jpeg', 'name': 'Samsung ultra', 'price': '70,000 Rs', 'condition': 'Used', 'location': 'Lahore'},
        {'id': 7, 'image': 'images/mobimg1.jpeg', 'name': 'Samsung ultra', 'price': '70,000 Rs', 'condition': 'Used', 'location': 'Lahore'},
        {'id': 8, 'image': 'images/mobimg1.jpeg', 'name': 'Samsung ultra', 'price': '70,000 Rs', 'condition': 'Used', 'location': 'Lahore'},
    ] 

    user = get_object_or_404(CustomUser, id=user_id)
    products = [
        {'id': 1, 'image': 'images/mobimg1.jpeg', 'name': 'Samsung ultra', 'price': '70,000 Rs', 'condition': 'New', 'location': 'Lahore'},
        # Add more products if needed
    ]  
    context = {
        'products': products,
        'user': user  # Pass user data to the template
    } 
    
    return render(request, 'main_marketplace.html', {'products': products})

# Description Page
def description_page(request):
    product = {
        'name': 'Samsung S22 Ultra  ',
        'price': 70000,
        'model': 'S12 g',
        'brand': 'Samsung',
        'condition': '2/258 GB',
        'availability': 'In Stock',
    }

    product_images = [
        {'id': 1,'image': 'images/mobimg1.jpeg'},
         {'id': 2,'image': 'images/mobimg1.jpeg'},

        
    ]

    related_models = [
        {'id': 1,'name': 'iPhone 16','image': 'images/mobimg1.jpeg'},
      
    ]

    productTableDesc = [
        {'label': 'Brand', 'value': 'Samsung'},
        {'label': 'Mobile Storage', 'value': '128 GB'},
        {'label': 'Battery Capacity', 'value': '4500 mAh'},
        {'label': 'Sim Type', 'value': 'Dual SIM'},
        {'label': 'Ram', 'value': '12 GB'},
        {'label': 'PTA Approved', 'value': 'Yes'},
        {'label': 'E-Sim', 'value': 'Yes'},
    ]

    context = {
        'product': product,
        'product_images': product_images,
        'related_models': related_models,
        'productTableDesc': productTableDesc,  # Pass this correctly to the template
    }

    return render(request, 'productDescriptionPage.html', context)

#signup page
def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'signup.html')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, 'signup.html')

        user = CustomUser(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
        )
        user.set_password(password)  # Hash the password before saving
        user.save()
        
        return redirect('marketplace:signin')
    
    return render(request, 'signup.html')


#signin page
def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)  # Use 'username' as 'email' here
        if user:
            login(request, user)
            return redirect('marketplace:main_marketplace', user_id=user.id)
        else:
            return render(request, 'signin.html', {"error": "Invalid email or password."})

    return render(request, 'signin.html')


def cart(request):
    return render(request, 'cart.html')

def bookingform(request):
    return render(request, 'bookingform.html')

def cart(request):
    return render(request, 'This is marketpalce cart page')


def bookingform(request):
    return render(request, 'bookingform.html')


