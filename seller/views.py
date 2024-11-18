from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from seller.models import ShopRegistration
from .models import Sale
from django.core.mail import send_mail
from django.conf import  settings
from django.core.mail import EmailMessage



# Frontpage view (no login required)
def frontpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.isSeller: 
                try:
                    shop = ShopRegistration.objects.get(user=user, isActive=True)
                    if shop:
                        login(request, user)
                        return redirect('seller:portal')
                except ShopRegistration.DoesNotExist:
                    messages.error(request, 'Your shop is not active.')
            else:
                messages.error(request, 'You do not have seller permissions.')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'front.html')

# Registration view
@login_required
def registration(request):
    if request.method == 'POST':
        shopname = request.POST.get('shopname')
        city = request.POST.get('city')
        area = request.POST.get('area')
        location = request.POST.get('location')
        
        if shopname and city and area and location:
            shop_registration = ShopRegistration(
                user=request.user,
                shopname=shopname,
                city=city,
                area=area,
                location=location
            )
            shop_registration.save()
            return redirect(reverse('seller:registerdone'))
        else:
            return render(request, 'registration.html', {'error': 'All fields are required.'})

    return render(request, 'registration.html')



def regdone(request):
     return render(request,'registerdone.html')

@login_required(login_url='/seller/')
def portal(request):
    try:
        shop = ShopRegistration.objects.get(user=request.user, isActive=True)
    except ShopRegistration.DoesNotExist:
        shop = None

    return render(request, 'portalbase.html', {'shop': shop})

@login_required(login_url='/seller/')
@login_required
def addproducts(request):
    return render(request, 'addproducts.html')

@login_required(login_url='/seller/')
@login_required
def listedproducts(request):
    return render(request, 'listedproducts.html')

@login_required(login_url='/seller/')
def ordermanagement(request):
     return render(request, 'orderManagement.html')

@login_required(login_url='/seller/')
def analytics(request):
    sales = Sale.objects.all().order_by('date')
    dates = [sale.date.strftime('%d %b') for sale in sales]
    amounts = [sale.amount for sale in sales]
    
    return render(request, "analytics.html", {'dates': dates, 'amounts': amounts})




@login_required(login_url='/seller/')
def support(request):
    try:
        # Get the users active shop registration
        shop = ShopRegistration.objects.get(user=request.user, isActive=True)
    except ShopRegistration.DoesNotExist:
        shop = None

    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('detail', '')
        user_email = request.user.email  # Get sender's email

        if shop:
            # Create the email message
            full_subject = f"{shop.shopname}: {subject}"
            
            # Format the message with additional details
            formatted_message = f"""
Support Ticket Details:
----------------------
From: {user_email}
Shop ID: {shop.shopID}
Shop Name: {shop.shopname}

Message:
{message}
            """
            
            try:
                # Create EmailMessage instance
                email = EmailMessage(
                    subject=full_subject,
                    body=formatted_message,
                    from_email=settings.EMAIL_HOST_USER,
                    to=['rajafajad0921@gmail.com'],
                    reply_to=[user_email]  # Set reply-to as user's email
                )
                
                # Send the email
                email.send(fail_silently=False)
                messages.success(request, "Your message has been sent successfully.")
                
            except Exception as e:
                messages.error(request, f"Failed to send email: {str(e)}")
        else:
            messages.error(request, "Your shop is not active. Please contact support.")

    # Prepare default values for the form fields
    default_shop_id = shop.shopID if shop else ''
    default_shop_name = shop.shopname if shop else ''
    default_email = request.user.email

    return render(request, 'support.html', {
        'default_shop_id': default_shop_id,
        'default_shop_name': default_shop_name,
        'default_email': default_email,
    })




@login_required(login_url='/seller/')
def mystore(request):
     return render(request, 'store.html')

@login_required(login_url='/seller/')
def payments(request):
     return render(request, 'payments.html')

@login_required(login_url='/seller/')
def accountsettings(request):
     return render(request, 'accountSettings.html')


