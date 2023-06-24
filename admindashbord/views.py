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
from .serializers import UserSerializer,ProductSerializer
from .models import Order,MainProduct
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random

from django.views.decorators.cache import never_cache
# Create your views here.
def base (request):
    return render (request,"admindashbord/orders.html")




def get_data (request):
    with open ("response_1686250644208.json",'r', errors='ignore', encoding='UTF-8') as json_data:
        data = json.load(json_data)
        for item in data:
            new_main_product = MainProduct(
                refrence_id = item['id'],
                title = item['title'],
                price = item['price'],
                inventory = item['inventory'],
                mainimage = f"https://jensokala.com{item['mainImage']}",
                active = item['active'],
                code = item['code'],
                postalCode = item['postalCode'],
            )
            if item['active'] is None  or item['active'] == "":
                new_main_product.active = False
            else:
                new_main_product.active =  item['active'] 
                
            new_main_product.save()



        # for item in data :
           
        #         # print (item)
        #         buyer = item['buyer']
        #         if buyer:
        #             addres = buyer['usersAdress']
        #         mali = item['mali']
        #         prudoct_list =['products']
        #         networker = item['network']
               
        #         if addres :
        #             useradress= CustomerAdress(
        #                 refrence_id= addres['id'] ,
        #                 address= addres['address'] ,
        #                 postal_code= addres['postalCode'] ,
        #                 state=addres['state']  ,
        #                 city=addres['city']  ,
        #                 recaiver_phonenumbr= addres['reciver'] ,
        #                 price=addres['price']  ,
        #                 texprice= addres['taxPrice'] ,
        #             )
        #             useradress.save()
        #         if buyer:
        #             buyer_datail = Buyer(
        #                 refrence_id =buyer['id'],
        #                 first_name= buyer['firstName'],
        #                 last_name= buyer['lastName'],
        #                 phone= buyer['mobile'],
                        
        #             )
        #             if addres:
        #                 buyer_datail.addres = useradress
        #             buyer_datail.save()
        #         peyment_datail = Peyment(
        #             ispayed = mali['isPayed'],

        #             total_payed_price =mali['totalPayedPrice'],
                    
        #             postpay= mali['postPay'],
                    
        #             tatolapaybypost= mali['totalPayedWithPostPrice'],
        #             shippingId = mali['shippingId'],
        #             shippingType = mali['shippingType'],
        #             shippingTypeString = mali['shippingTypeString'],
        #             deliveryDate = mali['deliveryDate'],
        #         )
        #         peyment_datail.save()

        #         products_objects = []
        #         for pro in item['products'] :
        #             new_pro = Product(
        #                 refrence_id = pro['id'],
        #                 title = pro['title'],
        #                 description = pro['description'],
        #                 price = pro['price'],
        #                 inventory = pro['inventory'],
        #                 mainImage = f"https://jensokala.com{pro['mainImage']}",
                        
        #                 code = pro['code'],
        #                 postalCode = pro['postalCode'],
        #                 quantity = pro['quantity'],

        #             )
        #             try :
        #                 new_pro.active=pro['active']
        #                 new_pro.save()
        #             except:
        #                 new_pro.active = True
        #                 new_pro.save()

        #             products_objects.append(new_pro)
                
        #         netwoeker_object = Networker (
        #             refrence_id = networker['id'],
        #             mobile = networker['mobile'],
        #             fullName = networker['fullName'],
        #             code = networker['code'],
        #         )
        #         netwoeker_object.save()

        #         order_object = Order(
        #             status = item['status'],
        #             refrence_id = item['id'],
        #             created = item['creationDate'],
        #             userid = item['userId'] ,
        #             basketid = item['basketId'], 
        #             quntity= item['quantity'],
        #             bayer= buyer_datail,
        #             mali=peyment_datail,
        #             networker=netwoeker_object,

        #         )
        #         order_object.save()
        #         order_object.products.set(products_objects)

                
        #         a+=1
         
    return HttpResponse({"status":"Fuck"})


def delete_object (request):
    MainProduct.objects.all().delete()
    # Buyer.objects.all().delete()
    # Peyment.objects.all().delete()
    # Product.objects.all().delete()
    # Networker.objects.all().delete()
    # Order.objects.all().delete()
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


@never_cache
@login_required(login_url="/")
def order_list(request):
    all_orders = Order.objects.all()

    order_list = Order.objects.all().order_by("-refrence_id")[0:300]
    call_status_list = CallStatus.objects.all()
    main_products = MainProduct.objects.all().order_by("-refrence_id")
    return render(request,"admindashbord/orders_list.html",{"order_list":order_list,"main_products":main_products,"call_status_list":call_status_list})

@login_required(login_url="/")
@never_cache
def order_detail(request,pk):
    order = Order.objects.get(refrence_id=pk)
    networker_id = Networker.objects.get(refrence_id=order.networker.refrence_id)
    history_order = networker_id.net_order.all()
    context = {
        "order":order,
        "status":[   
        "در صف بررسی",
         "آماده‌سازی سفارش",
         "تایید سفارش",
         "خروج از مرکز پردازش",
         "تحویل به پست",
         "تحویل مرسوله به مشتری",
         "مرجوع شده",
         "بدون وضعیت"
         ],
        "call_status" :CallStatus.objects.all(),
        "history_orders":history_order,
        "main_prodacts" :MainProduct.objects.all().order_by("-refrence_id")
    }
    
    return render(request,"admindashbord/order_detail.html",context)


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
   
        
        


					
@api_view(['GET'])
def change_call_status(request):
    if request.GET:
        order_id = request.GET.get('order_id')
        select_id = request.GET.get('select_id')
        order = Order.objects.get(refrence_id=order_id)
        call_status = CallStatus.objects.get(id=select_id)
        order.call_status = call_status
        order.save()
        return Response(status=status.HTTP_200_OK,data={"message":"success"})

@csrf_exempt 
def Delete_Order(request):
    if request.POST:
       
        order_id = request.POST.get('id')
        order = Order.objects.get(refrence_id=order_id)
        order.delete()
        return JsonResponse({"message":"success"})
    


@api_view(['GET'])
def product_read_detail(request,pk):
    if request.method == 'GET':
        product = Product.objects.get(refrence_id=pk)
        return Response(status=status.HTTP_200_OK,data=ProductSerializer(product).data)


@api_view(['POST'])
def create_order (request):
    if request.POST:
        data = request.data
        # print(data)
        products = request.POST.getlist('products')
        first_name = data['first-name']
        last_name = data['last-name']
        ostan = data['ostan']
        city = data['city']
        addres = data['addres']
        phone_number = data['phone_number']
        # print(products)
        price = 0
        pro_order_list = []
        for product_id in products:
            number = data[f"{product_id}"]
            pro_object = MainProduct.objects.get(id =product_id)
            
            price += int(pro_object.price) * int(number)
            
            
            
            new_pro_order = Product(
                refrence_id = pro_object.refrence_id,
                title = pro_object.title,
                price= pro_object.price,
                postalCode=pro_object.postalCode,
                mainImage = pro_object.mainimage,
                inventory = number,
                code =pro_object.code
                

            )
            new_pro_order.quantity = int(pro_object.price) * int(number)
            new_pro_order.save()
            pro_order_list.append(new_pro_order)
        
            
        return Response({"Status":"Fuck"})
    

@api_view(["GET"])
def update_order_product(request,pk):
    if request.GET:
        data = request.GET
        number = int(data.get('number'))
        number_main = int(data.get('number'))
        product_id = data.get('product_id')
        number_main = - number_main
        product_query = Product.objects.get(refrence_id=product_id)
        product_query.inventory = number_main
        product_query.save()

        order_object = Order.objects.get(refrence_id=pk)
        all_price = 0
        for pro in order_object.products.all():
            inv_main = pro.inventory
            inv_main = -inv_main
            all_price+= int(pro.price) * inv_main
        order_object.mali.total_payed_price = all_price
        order_object.mali.tatolapaybypost = all_price
        order_object.mali.save()
        
        return Response(status=status.HTTP_202_ACCEPTED,data={"all_price":all_price})



@api_view(["GET"])
def get_order_price(request,pk):
  
    order_object = Order.objects.get(refrence_id=pk)
 
    return Response(status = status.HTTP_200_OK,data = {"order_price":order_object.mali.total_payed_price})
# MainProduct
# refrence_id
# title
# price
# mainimage
# code
# postalCode

# Product
# title
# description
# price
# mainImage
# active
# code
# postalCode

@api_view(['POST'])
def add_product_to_order(request,order_id):
    if request.POST:
        data =request.data
        product = data['product']
        count = data['count']
        countneg = int(data['count'])
        main_pro = MainProduct.objects.get(refrence_id = product)   
        order = Order.objects.get(refrence_id = order_id)
        num = "545646515"
        code ="".join(random.sample(num,5))
        new_pro_order = Product(
            refrence_id = code,
            title =main_pro.title,
            price = main_pro.price ,
            mainImage = main_pro.mainimage ,
            code =  main_pro.code,
            postalCode =  main_pro.postalCode,
        )
        countneg = - countneg
        new_pro_order.inventory = countneg
        new_pro_order.save()


        order.products.add(new_pro_order)
        qun_price = 0
        for item in order.products.all():
            inv_fake = item.inventory
            inv_fake = -inv_fake
            qun_price += int(item.price) * int (inv_fake)
        order.mali.total_payed_price = qun_price
        order.mali.tatolapaybypost = qun_price
        order.mali.save()
        



        return Response(status=status.HTTP_201_CREATED,data={"message":"success"})
    


@api_view(['GET'])
def change_status_order(request,order_id):
    if request.GET:
        data = request.GET

        status_order = data.get('status_order')

        order_object = Order.objects.get(refrence_id=order_id)
        order_object.status = status_order
        order_object.save()
        return Response(status= status.HTTP_202_ACCEPTED,data= {"message":"succses"})
    
@api_view(['GET'])
def change_call_status_order(request,order_id):
    if request.GET:
        data= request.GET
        order_object = Order.objects.get(refrence_id=order_id)
        call_status= data.get("call_status")
        call_status_object = CallStatus.objects.get(id=call_status)
        order_object.call_status = call_status_object
        order_object.save()
        return Response(status=status.HTTP_202_ACCEPTED,data = {"message":"success"})

@api_view(['POST'])
def create_addres_order(request, order_id):
    if request.POST:
        data= request.data
        first_name = data['first_name']
        last_name = data['last_name']
        ostan = data['ostan']
        city = data['city']
        addres = data['addres']
        phone_number = data['phone_number']
        postcode = data['postcode']
        order_object = Order.objects.get(refrence_id =order_id)
        order_object.bayer.first_name = first_name
        order_object.bayer.last_name = last_name
        order_object.bayer.phone =phone_number
        order_object.bayer.save()
        order_object.bayer.addres.address = addres
        order_object.bayer.addres.postal_code = postcode
        order_object.bayer.addres.state = ostan
        order_object.bayer.addres.city = city
        order_object.bayer.addres.save()
        return Response(status=status.HTTP_201_CREATED,data={"message":"success"})