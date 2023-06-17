from django.db import models
from persian_date.utils import jalali_converter
from jalali_date import datetime2jalali, date2jalali



class CustomerAdress(models.Model):
    refrence_id = models.BigIntegerField(unique=True,primary_key=True)
    address = models.TextField(null=True)
    postal_code = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    recaiver_phonenumbr = models.CharField(max_length=200,null=True)
    price= models.CharField(max_length=200,null=True)
    texprice = models.CharField(max_length=200,null=True)
class Buyer (models.Model):
    refrence_id = models.BigIntegerField(unique=True,primary_key=True)
    first_name = models.CharField(max_length=200,null=True)

    last_name = models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    addres=models.ForeignKey(CustomerAdress,on_delete=models.CASCADE,null=True)



class Peyment(models.Model):
    ispayed = models.BooleanField(default=False)
    total_payed_price = models.CharField(max_length=200,null=True)
    postpay=models.CharField(max_length=200,null=True)
    tatolapaybypost= models.CharField(max_length=200,null=True)
    shippingId =models.IntegerField(null=True)
    shippingType=models.CharField(null=True,max_length=200)
    shippingTypeString=models.CharField(max_length=200,null=True)
    deliveryDate=models.CharField(max_length=200,null=True)


class Product (models.Model):
        refrence_id = models.BigIntegerField (unique=True,primary_key=True)
        title = models.CharField(max_length=250,null=True)
        description = models.TextField()
        price = models.CharField(max_length=250,null=True)
        inventory = models.IntegerField(null=True)
        mainImage = models.URLField(null=True)
        active = models.BooleanField(default=False)
        code = models.CharField(max_length=250,null=True)
        postalCode = models.CharField(max_length=250,null=True)
        quantity = models.IntegerField(null=True)



class Networker (models.Model):
    refrence_id = models.BigIntegerField (unique=True,primary_key=True)
    mobile = models.CharField(max_length = 255,null=True)
    fullName = models.CharField(max_length = 255,null=True)
    code = models.CharField(max_length = 255,null=True)


class CallStatus(models.Model):
     title = models.CharField(max_length=250,null=True)
     color_code = models.CharField(max_length=250,null=True)


class Order (models.Model):
    role = (
         ("در صف بررسی","در صف بررسی"),
         ("آماده‌سازی سفارش","آماده‌سازی سفارش"),
         ("تایید سفارش","تایید سفارش"),
         ("خروج از مرکز پردازش","خروج از مرکز پردازش"),
         ("تحویل به پست","تحویل به پست"),
         ("تحویل مرسوله به مشتری","تحویل مرسوله به مشتری"),
         ("مرجوع شده","مرجوع شده"),
         ("بدون وضعیت","بدون وضعیت")


    )
    call_status = models.ForeignKey(CallStatus,on_delete=models.CASCADE,null=True,related_name="orders")
    status = models.CharField(max_length=50, choices = role, default = 'بدون وضعیت')
    refrence_id = models.BigIntegerField(unique=True,primary_key=True)
    created = models.CharField(max_length=250,null=True)
    userid = models.IntegerField(null=True)
    basketid = models.IntegerField(null=True)
    bayer  = models.ForeignKey(Buyer,on_delete=models.CASCADE,null=True)
    mali = models.ForeignKey(Peyment,on_delete=models.CASCADE,null=True)
    quntity = models.CharField(max_length=200,null=True)
    networker = models.ForeignKey(Networker,on_delete=models.CASCADE,null=True)
    products = models.ManyToManyField(Product)
    done = models.BooleanField(default=False)
    created_main = models.DateTimeField(auto_now_add=False,null=True)

    def netwoker_name(self):
         return self.networker.fullName



    def created_data(self):
        return datetime2jalali(self.created).strftime('%y/%m/%d _ %H:%M:%S')
        

    def cutting_pirce(self):
       return self.mali.total_payed_price
    


