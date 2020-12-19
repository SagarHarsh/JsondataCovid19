from django.contrib import admin
from django.urls import path
from app21 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.covid,name='covid'),
    path('showdata',views.showdata,name='showdata'),
    path('medicalcollage/',views.medicalcollage,name='medicalcollage'),
    path('contact/',views.contact,name='contact'),


]