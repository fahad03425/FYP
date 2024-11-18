from django.contrib import admin
from .models import ShopRegistration

# Register your models here.
from .models import Sale

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount')  # This will display these fields in the list view
    list_filter = ('date',)  # Allows filtering by date
    search_fields = ('date',)  # Allows searching 

@admin.register(ShopRegistration)
class ShopRegistrationAdmin(admin.ModelAdmin):
   # Update list_display fields to match model fields
    list_display = ('shopID', 'user', 'shopname', 'city', 'area', 'location', 'isActive', 'creation_date', 'last_update')
    # Update search fields and list filters to match model fields
    search_fields = ('shopname', 'city', 'area', 'user__username')  # Assuming 'user' is a ForeignKey to a User model
    list_filter = ('city', 'isActive', 'creation_date')

    # Specify fields in detail view, and correct field names for readonly_fields
    fields = ('shopID', 'user', 'shopname', 'city', 'area', 'location', 'creation_date', 'last_update', 'isActive')
    readonly_fields = ('creation_date', 'last_update')  # Ensure these fields exist in the model


