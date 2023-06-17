from django.shortcuts import render,redirect
from .models import * 
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from users_app.models import UserAccount
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from .serializers import UserSerializer
from .models import Order
from django.http import JsonResponse
import json
# Create your views here.
def base (request):
    return render (request,"admindashbord/orders.html")




def get_data (request):
    with open ("response_1686250644208.json",'r', errors='ignore', encoding='UTF-8') as json_data:
        data = json.load(json_data)
        a=0
        



        for item in data :
           
                # print (item)
                buyer = item['buyer']
                if buyer:
                    addres = buyer['usersAdress']
                mali = item['mali']
                prudoct_list =['products']
                networker = item['network']
               
                if addres :
                    useradress= CustomerAdress(
                        refrence_id= addres['id'] ,
                        address= addres['address'] ,
                        postal_code= addres['postalCode'] ,
                        state=addres['state']  ,
                        city=addres['city']  ,
                        recaiver_phonenumbr= addres['reciver'] ,
                        price=addres['price']  ,
                        texprice= addres['taxPrice'] ,
                    )
                    useradress.save()
                if buyer:
                    buyer_datail = Buyer(
                        refrence_id =buyer['id'],
                        first_name= buyer['firstName'],
                        last_name= buyer['lastName'],
                        phone= buyer['mobile'],
                        
                    )
                    if addres:
                        buyer_datail.addres = useradress
                    buyer_datail.save()
                peyment_datail = Peyment(
                    ispayed = mali['isPayed'],

                    total_payed_price =mali['totalPayedPrice'],
                    
                    postpay= mali['postPay'],
                    
                    tatolapaybypost= mali['totalPayedWithPostPrice'],
                    shippingId = mali['shippingId'],
                    shippingType = mali['shippingType'],
                    shippingTypeString = mali['shippingTypeString'],
                    deliveryDate = mali['deliveryDate'],
                )
                peyment_datail.save()

                products_objects = []
                for pro in item['products'] :
                    new_pro = Product(
                        refrence_id = pro['id'],
                        title = pro['title'],
                        description = pro['description'],
                        price = pro['price'],
                        inventory = pro['inventory'],
                        mainImage = f"https://jensokala.com{pro['mainImage']}",
                        
                        code = pro['code'],
                        postalCode = pro['postalCode'],
                        quantity = pro['quantity'],

                    )
                    try :
                        new_pro.active=pro['active']
                        new_pro.save()
                    except:
                        new_pro.active = True
                        new_pro.save()

                    products_objects.append(new_pro)
                
                netwoeker_object = Networker (
                    refrence_id = networker['id'],
                    mobile = networker['mobile'],
                    fullName = networker['fullName'],
                    code = networker['code'],
                )
                netwoeker_object.save()

                order_object = Order(
                    status = item['status'],
                    refrence_id = item['id'],
                    created = item['creationDate'],
                    userid = item['userId'] ,
                    basketid = item['basketId'], 
                    quntity= item['quantity'],
                    bayer= buyer_datail,
                    mali=peyment_datail,
                    networker=netwoeker_object,

                )
                order_object.save()
                order_object.products.set(products_objects)

                
                a+=1
         
    return HttpResponse({"status":"Fuck"})


def delete_object (request):
    CustomerAdress.objects.all().delete()
    Buyer.objects.all().delete()
    Peyment.objects.all().delete()
    Product.objects.all().delete()
    Networker.objects.all().delete()
    Order.objects.all().delete()
    return HttpResponse({"status":"Fuck"})



@login_required(login_url="/")
def home_page (request):
    # if request.user.is_admin:
        

    return render (request, "admindashbord/home_page.html",{"status":"Fuck"})

@login_required(login_url="/")
def logout_user(request):
    logout(request)

    return redirect("/")



@login_required(login_url="/")
def users_list(request):
    users = UserAccount.objects.all().order_by("-id")
    return render (request,"admindashbord/users_list.html",{"users":users})

@api_view(['GET'])
def change_status_user(request,pk):
    if request.GET:
        
        checked = request.GET.get("checked")
        if checked:
            user = UserAccount.objects.get(id=pk)
            user.is_active = True
            user.save()
            return Response (status=status.HTTP_200_OK,data={"message":"success"})
        else:
            user = UserAccount.objects.get(id=pk)
            user.is_active  = False
            user.save()
            return Response (status=status.HTTP_200_OK,data={"message":"success"})
# {'first_name': ['مرادی نیا'],
#   'last_name': ['مرادی نیا'], 
#   'username': ['تناتن'],
# 'phone_nmber': ['854654'], 'user_type': ['مدیر'], 
# 'csrfmiddlewaretoken': ['BAhqvkeYTv0cYdmzSA7x4eXmYtLc2FIZLtduCerTPvaDf7lvYkFg02naphHl5YsU']و
# 'password': ['123456'], 
# 'confirm_password': ['123456'],
#  'is_active': ['on']}>   

@api_view(['POST'])
def craete_user (request):
    if request.POST:
        data =request.data
        first_name = data['first_name']
        user_type =data['user_type']
        last_name = data['last_name']
        username = data['username']
        phone_nmber = data['phone_nmber']
        password = data['password']
        confirm_password = data['confirm_password']
        is_active = data['is_active']
        if len(password)  < 8 : 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,data={"message":"رمز عبور شما باید بیشتر از هشت رقم باشد"})
        if password  == confirm_password:
            try :
                user = UserAccount.objects.get(username=username)
                return Response(status=status.HTTP_401_UNAUTHORIZED,data={"message":"نام کاربری انتخاب شده درحال حاظر وجود دارد"})
            except:
                new_user = UserAccount(
                    firstname = first_name, 
                    lastname = last_name, 
                    username = username, 
                    phone_number =phone_nmber,
                    password=password,
                    user_type = user_type,
                )

                new_user.save()

                new_user.set_password(password)
                if is_active != "on":
                    new_user.is_active = False
                new_user.save()
                data_serializer = UserSerializer(new_user)

                print(data_serializer.data)
                
                return Response(status = status.HTTP_201_CREATED,data=data_serializer.data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,data={"message":"رمز عبور ها با هم تطابق ندارند"})
        
a= {'first_name': ['مجید'], 
             'last_name': ['بچک'], 
             'username': ['majidbachak'], 
             'phone_nmber': ['09385200120'], 
             'user_type': ['کال سنتر'], 
               'is_active': ['on']}

@api_view(['GET'])
def edit_user(request,pk):
    if request.GET:
        data = request.GET
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        phone_nmber = data.get('phone_nmber')
        user_type = data.get('user_type')
        is_active = data.get('is_active')
        user_main = UserAccount.objects.get(id=pk)
        if username != user_main.username:
            try:
                test_user = UserAccount.objects.get(username=username)
          
                return Response(status=status.HTTP_402_PAYMENT_REQUIRED, data={"message":"نام کاربری مورد نظر در حال حاظر وجود دارد"})
            except:
                user_main.firstname = first_name
                user_main.lastname = last_name
                user_main.username = username
                user_main.phone_number = phone_nmber
                user_main.user_type = user_type
                if is_active == "on":
                    user_main.is_active = True
                else:
                    user_main.is_active = False
                user_main.save()
        else:
                user_main.firstname = first_name
                user_main.lastname = last_name
           
                user_main.phone_number = phone_nmber
                user_main.user_type = user_type
                if is_active == "on":
                    user_main.is_active = True
                else:
                    user_main.is_active = False
                user_main.save()
            
        

                return Response(status=status.HTTP_202_ACCEPTED,data={"message":"کاربر مورد نظر با موفقین ادیت شد"})
        

@api_view(['GET'])
def delete_user(request,pk):
    
        user = UserAccount.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_202_ACCEPTED,data={"message":"کاربر موورد نظر با موفقیت ادیت شد"})




def order_list(request):
    all_orders = Order.objects.all()

    order_list = Order.objects.all().order_by("-refrence_id")
    call_status_list = CallStatus.objects.all()
    return render(request,"admindashbord/orders_list.html",{"order_list":order_list,"call_status_list":call_status_list})



def crete_order_template(request):
    context = {}
    products = Product.objects.all()
    return render(request,"admindashbord/create_order.html")


@api_view(['GET'])
def read_orders (request):
  
 
    
        orders = Order.objects.all()
        data = []

        for order in orders :
            dic = {
                "id" : order.refrence_id,
                "networker_name":order.networker.fullName,
                "price": order.mali.total_payed_price,
                "data" : order.created,
                "status": order.status,
                

            }
            call_status_list = []
            for call_statis_query in CallStatus.objects.all():
                dic_cl_status={}
                if call_statis_query.id == order.call_status.id:
                    dic_cl_status['c_status_title'] = call_statis_query.title
                    dic_cl_status['c_status_id'] = call_statis_query.id
                    dic_cl_status['selected'] = True
                else:
                    dic_cl_status['c_status_title'] = call_statis_query.title
                    dic_cl_status['c_status_id'] = call_statis_query.id
                    dic_cl_status['selected'] = False
                call_status_list.append(dic_cl_status)
            dic['call_status'] = call_status_list
            data.append(dic)
      
        return Response (status = status.HTTP_200_OK,data= data)
   
        
        


					
