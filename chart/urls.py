from django.urls import path

from . import views

from chart import *

urlpatterns = [
    path('', views.index, name='index'),
    path('gigi', views.read_from_mysql, name='read_from_mysql'),
]

#read_serial_data()