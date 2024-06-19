# users/models.py
from django.db import models
#from algerography.models import Wilaya
from django.contrib.auth.models import AbstractUser

class custom_user(AbstractUser):
    phone_num = models.CharField(max_length=15)
    profile_pic = models.ImageField(upload_to='user_pic/')
    def __str__(self):
        return self.username
class Wilaya(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
class Product(models.Model):
    user = models.ForeignKey("custom_user", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    STATE_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
    ]
    state = models.CharField(max_length=4, choices=STATE_CHOICES)
    #def get_city_choices():
     #   return [(wilaya.name, wilaya.name) for wilaya in Wilaya.objects.all()]
    
    #CITY_CHOICES = get_city_choices()
    #city = models.CharField(max_length=255, choices=CITY_CHOICES)
    city = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)  # New field
    sales = models.PositiveIntegerField(default=0)

    
    
    def __str__(self):
        return self.name

class media_files(models.Model):
    product_id = models.ForeignKey("Product",on_delete=models.CASCADE)
    path = models.ImageField(upload_to='post_pic/')

