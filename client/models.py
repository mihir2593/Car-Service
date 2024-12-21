import uuid
from django.contrib.auth.models import User
from django.db import models

from storesapp.models import storemodel

from storesapp.models import productmodel


# Create your models here.
class userdetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()


class servicerequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(storemodel, on_delete=models.CASCADE)
    c_name = models.CharField(max_length=100)
    c_email = models.EmailField()
    c_phonenumber = models.BigIntegerField()
    date = models.DateField()
    service_type = models.TextField()
    status = models.CharField(max_length=255,default="pending")


class cartitem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    productname = models.CharField(max_length=230)
    quantity = models.IntegerField()
    price = models.IntegerField()



class FinalOrder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total = models.BigIntegerField()
    gst = models.BigIntegerField()
    finaltotal = models.BigIntegerField()

class confirmorder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    final=models.ForeignKey(FinalOrder,on_delete=models.CASCADE)
    product = models.ForeignKey(productmodel,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()


class allorderlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    productname = models.CharField(max_length=230)
    quantity = models.IntegerField()
    price = models.IntegerField()


class wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    productname = models.CharField(max_length=230)
    price = models.IntegerField()





