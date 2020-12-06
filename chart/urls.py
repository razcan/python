from django.urls import path

from . import views

from chart import *

urlpatterns = [
    path('', views.index, name='index'),
    path('gigi', views.read_from_mysql, name='index'),
    path('read', views.read_data, name='read_data'),
]

#read_serial_data()