from django.urls import path 
from .views import *
app_name = "callcenter_dashbord"
urlpatterns = [
    path ('HomePage',home_page,name="home_page")
]
