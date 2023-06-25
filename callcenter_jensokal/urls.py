
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings
urlpatterns = [
    path('manager/manageruser', admin.site.urls),
    path ('admindashboard/', include('admindashbord.urls')),
    path ('CallCenterDashbord/', include('callc_dashbord.urls')),
    path ('', include('users_app.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
