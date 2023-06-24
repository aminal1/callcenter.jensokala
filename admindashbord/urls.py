from django.urls import path

from . import views
app_name = "admindashbord"
urlpatterns = [
    path("base",views.base),
    path("get_data",views.get_data),
    path("delete_object",views.delete_object),
    path("home_page",views.home_page,name="home_page"),
    path("logout_user",views.logout_user , name="logout_user"),
    path("users_list",views.users_list , name="users_list"),
    path("change_status_user/<int:pk>",views.change_status_user,name = "change_status_user"),
    path("craete_user",views.craete_user , name="craete_user"),
    path("edit_user/<int:pk>",views.edit_user,name = "edit_user"),
    path("delete_user/<int:pk>",views.delete_user,name = "delete_user"),
    path("order_list",views.order_list,name = "order_list"),
    path("order_detail/<int:pk>",views.order_detail,name = "order_detail"),
    path("read_orders",views.read_orders,name = "read_orders"),
    path("change_call_status",views.change_call_status,name = "change_call_status"),
    path("Delete_Order",views.Delete_Order,name = "Delete_Order"),
    path("product_read_detail/<int:pk>",views.product_read_detail,name = "product_read_detail"),
    path("create_order",views.create_order,name = "create_order"),
    path("update_order_product/<int:pk>",views.update_order_product,name = "update_order_product"),
    path("get_order_price/<int:pk>",views.get_order_price,name = "get_order_price"),
    path("add_product_to_order/<int:order_id>",views.add_product_to_order,name = "add_product_to_order"),
    path("change_status_order/<int:order_id>",views.change_status_order,name = "change_status_order"),
    path("change_call_status_order/<int:order_id>",views.change_call_status_order,name = "change_call_status_order"),
    path("create_addres_order/<int:order_id>",views.create_addres_order,name = "create_addres_order"),



]