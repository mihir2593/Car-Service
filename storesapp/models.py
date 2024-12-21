from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class categorymodel(models.Model):

    company = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    model_year = models.IntegerField()

class usecategorymodel(models.Model):
    usecategory = models.CharField(max_length=100)
    where_to_use = models.TextField(max_length=200)

class productmodel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Cate = models.ForeignKey(categorymodel, on_delete=models.CASCADE)
    Usecate = models.ForeignKey(usecategorymodel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product')
    price = models.IntegerField()
    isavailable = models.BooleanField(default=True)
    is_wished = models.BooleanField(default=False)






# -------For Services --------------
class storemodel(models.Model):
    s_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    s_phonenumber = models.BigIntegerField()
    email = models.EmailField()
    o_time = models.TimeField()
    c_time = models.TimeField()
    isavailable = models.BooleanField(default=True)





