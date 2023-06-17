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
    path("crete_order",views.crete_order_template,name = "crete_order"),
    path("read_orders",views.read_orders,name = "read_orders"),



]