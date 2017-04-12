from django.conf.urls import url,include
from django.contrib import admin
from My_profile import views


urlpatterns = [
    #url(r'^', views.Name_view),
    url(r'^address', views.Address_view),
    url(r'^contact', views.contact),
    url(r'^', views.Name_view),

]
