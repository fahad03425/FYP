from django.db import models
from marketplace.models import CustomUser  # Import the CustomUser model from marketplace app
from django.conf import settings
from django.utils import timezone
import random

# Create your models here.

class Sale(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale on {self.date} - PKR {self.amount}"
    
#                                             Shop Registration
    
def generate_shop_id():
    return random.randint(100000, 999999)
    
class ShopRegistration(models.Model):
    shopID = models.IntegerField(default=generate_shop_id)
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="shops"
     )
    shopname = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    area = models.TextField(max_length=100)
    location = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.shopname
