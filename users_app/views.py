from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserAccount
from rest_framework import status
from django.contrib.auth import authenticate,login

# Create your views here.
def user_login (request):
    if request.user.is_authenticated:
        if request.user.user_type:
            return redirect ("admindashbord:home_page")
        
    return render (request,'users_app/login.html')

@api_view(['POST'])
def api_login (request):
    if request.POST:
        data= request.data
        username = data.get('email')
        password = data.get('password')
 
        try : 
            user= UserAccount.objects.get(username=username)
            
            authuser = authenticate(username = username, password=password)
           
            if authuser :
                if user.is_admin:
                    login(request,authuser)
                     
                    return Response({"message":"ورود به حساب کاربری با موفقیت انجام شد","redirect_url":"/admindashboard/home_page"},status=status.HTTP_200_OK)
                else:
                    return Response({"message":"ورود به حساب کاربری با موفقیت انجام شد","redirect_url":"/CallCenterDashbord/HomePage"})
            else:
                    return Response({"message":" رمز عبور اشتباه است"},status=status.HTTP_400_BAD_REQUEST)
        except :
            return Response ({"message":"کاربر مورد نظر وجود ندارد"},status=status.HTTP_400_BAD_REQUEST)
        



def register_user (request):
    return render (request,"users_app/register.html")


@api_view(['POST'])
def create_user(request):
    if request.POST:
        data =request.data


        first_name = data['first-name']
        last_name = data['last-name']
        username = data['email']
        phone_number = data['phone_number']
        password = data['password']

        try :
            test_username = UserAccount.objects.get(username=username)
            return Response(status = status.HTTP_401_UNAUTHORIZED,data={"message":"نام کربری انتخاب شده در حال حاضر وجود دارد"})
        except:
            new_user = UserAccount(
                firstname = first_name,
                lastname = last_name,
                phone_number=phone_number,
                username=username,
                
                
            )
            new_user.save()
            new_user.set_password(password)
            new_user.is_admin = False
            new_user.save()
            login(request,new_user)
            
            return Response(status=status.HTTP_201_CREATED,data={"message":"ثیت نام با موفقیت انجام شد"})




