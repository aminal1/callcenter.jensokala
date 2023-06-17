from django.urls import path 
from . import views
app_name = "users_app"
urlpatterns = [
    path ("",views.user_login,name = "user_login"),
    path ("api_login",views.api_login,name = "api_login"),
    path ("register_user",views.register_user,name = "register_user"),
    path ("create_user",views.create_user,name = "create_user"),
   
]

