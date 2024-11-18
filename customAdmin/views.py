
from django.shortcuts import render, get_object_or_404, redirect
from seller.models import ShopRegistration
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import logging

# Create your views here.

logger = logging.getLogger(__name__)

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:  # Check if the user is a superuser
                login(request, user)  # Log the user in
                return redirect('customAdmin:dashboard')  # Redirect to the admin dashboard
            else:
                messages.error(request, 'You do not have permission to access this page.')  # Show error for non-superusers
        else:
            messages.error(request, 'Invalid username or password.')  # Show error for invalid credentials
            logger.warning(f'Failed login attempt for username: {username}')  # Log the failed attempt

    return render(request, 'adminlogin.html')


@login_required
def dashboard(request):
    if not request.user.is_superuser:
        return redirect('customAdmin:customAdmin')  # Redirect if not a superuser

    # Your dashboard logic here
    return render(request, 'dashboard.html')


def registeredSellers(request):
    if request.method == 'POST':
        # Handle the delete request
        shop_id = request.POST.get('shop_id')
        if shop_id:
            shop = get_object_or_404(ShopRegistration, shopID=shop_id)
            # Deactivate the shop and user
            shop.isActive = False
            shop.user.is_seller = False
            shop.user.save()  # Save the user changes
            shop.save()  # Save the shop changes
            
            # Optionally add a success message or log action
            # messages.success(request, 'Seller deactivated successfully.')
            return redirect('customAdmin:registeredSellers')  # Redirect back to the sellers list

    # Fetch all active sellers
    sellers = ShopRegistration.objects.filter(isActive=True)
    return render(request, 'registeredsellers.html', {'sellers': sellers})
    

def registeredsellerdetails(request, shopID):
    seller = get_object_or_404(ShopRegistration, shopID=shopID)
    user = seller.user
    
    
    # Render the template with seller and user details for a GET request
    return render(request, 'registeredsellerdetails.html', {'seller': seller, 'user': user})
    
  

def newsellers(request):
    sellers = ShopRegistration.objects.filter(isActive=False)  # Modify this filter if needed
    return render(request, 'newsellers.html', {'sellers': sellers})


def newsellerdetail(request, shopID):
    seller = get_object_or_404(ShopRegistration, shopID=shopID)
    user = seller.user
    
    # Check if this is a POST request for approval
    if request.method == 'POST':
        seller.isActive = True  # Set shop as active
        user.isSeller = True    # Set user as a seller
        seller.save()
        user.save()
        return redirect('customAdmin:newsellers')  # Redirect to new sellers page after approval
    
    # Render the template with seller and user details for a GET request
    return render(request, 'newsellerdetail.html', {'seller': seller, 'user': user})


def addphone(request):
    return render(request, 'addphone.html')

def category(request):
    return render(request, 'categories.html')

def brand(request):
    return render(request, 'brand.html')

def model(request):
    return render(request, 'model.html')

def specification(request):
    return render(request, 'specification.html')

def adminsettings(request):
    return render(request, 'adminsettings.html')
    
