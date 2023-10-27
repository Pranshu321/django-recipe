from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField()
    address = models.TextField()

# pre_save signal
# post_save signal
# pre_delete signal
# post_delete signal

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name

@receiver(post_save , sender=Product)    
def call_car_api(sender , instance , **kwargs):
    print("CAR OBJECT CREATED")
    print(sender , instance , kwargs)

