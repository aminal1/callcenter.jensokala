
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from persian_date.utils import jalali_converter


class UserAccountManager(BaseUserManager):
    def create_user(self,username,firstname,city,lastname,state,email,password):
        if not username:
            raise ValueError("enter all fieldes")

        else:
            user = self.model(firstname=firstname,city=city,lastname=lastname,state=state,email=email,password=password)
            
            user.is_admin = False
            user.set_password(password)
            user.save()


            return user




    def create_superuser(self,username,password,
                         firstname,lastname):

        user = self.model(username=username,firstname=firstname,lastname=lastname)
        
        user.save()
        user.user_type='مدیر'
        user.set_password(password)
        user.save()
        return user

        


class UserAccount(AbstractBaseUser):
    role = (
        ("کال سنتر","کال سنتر"),
        ("مدیر","مدیر")
    )
    user_type = models.CharField(max_length=50, choices = role, default = 'کال سنتر')
    firstname =models.CharField(max_length=255,null=True,blank=True)
    lastname =models.CharField(max_length=255,null=True,blank=True)
    phone_number = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique =True)
    password = models.CharField(max_length=255)
    city= models.CharField(max_length=255 ,null=True)
    state = models.CharField(max_length=255,null=True)
    secret_key =models.CharField(max_length=255,null=True,blank=True)
    created= models.DateField(auto_now_add=True,null=True)


    


    is_active =models.BooleanField(default =True)
    is_admin = models.BooleanField(default =True)
    is_staff = models.BooleanField(default =True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =['firstname','lastname']


    objects = UserAccountManager()



    def has_perm (self,perm,obj=None):
        return True


    def created_data(self):
       return  jalali_converter(self.created)

    def has_module_perms(self,app_label):
        return True

    def __str__(self):
       
        return self.username
   
    # def jtime(self):
    #     return jalali_converter(self.created)
    




