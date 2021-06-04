from django.contrib import admin
from django.urls import path,include
from .views import home,center_list,district_list

urlpatterns = [
    path("/all",center_list,name="center_list"),
    path("/district",district_list,name="district_list")
]
