from django.shortcuts import render 
from django.http import HttpResponse
import mysql.connector
import serial
import time
from mysql.connector import errorcode
from django.db import models
from chart.models import *
from django.urls import path
from . import views
from django.template.response import TemplateResponse
from datetime import date
import datetime
from django.conf import settings
from django.utils.timezone import make_aware


def index(request, template_name="index.html"):
    args = {}
    text = "hello world"
    args['mytext'] = "text"
    return TemplateResponse(request, template_name, args)

def read_from_mysql(request, template_name="index.html"):
    #  mydb = mysql.connector.connect(
    #     host="localhost",
    #     user="admin",
    #     password="vasilica",
    #     database="RZC"
    #     )

    #  mycursor = mydb.cursor()   
    #  mycursor.execute("SELECT * FROM chart_info")
     #myresult = mycursor.fetchall()
     #print(myresult)
    #  args = {}
    #  text = "hello world"
    #  args['mytext'] = text
     #Reserved.objects.filter(client=client_id).order_by('-check_in')
     #myresult = list(Info.objects.all())  
     labels = []
     data = []
     queryset = Info.objects.filter().order_by('-id')[:10]
     myresult = Info.objects.filter().order_by('-id')[:10]
     for measure in queryset:
        labels.append(measure.id)
        data.append(measure.distance)

     return TemplateResponse(request, template_name, {
        "myresult" : myresult,
        "labels" : labels,
        "data": data,
                                                     })

def read_data(request):
    today = date.today()
    z1baudrate = 9600
    z1port = '/dev/ttyUSB0'  # set the correct port before run it

    z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
    z1serial.timeout = 20 # set read timeout

    z1serial.flushInput()
    z1serial.flushOutput()
    
    if z1serial.is_open:
        while True:
            data_raw = z1serial.readline()
            info = Info()
            info.distance = data_raw.decode("utf-8")
            #info.time = time.strftime('%Y-%m-%d %H:%M:%S')         
            naive_datetime = datetime.datetime.now()
            naive_datetime.tzinfo  # None
            settings.TIME_ZONE  # 'UTC'
            aware_datetime = make_aware(naive_datetime)
            aware_datetime.tzinfo  # <UTC>
            info.time = aware_datetime
            info.save()


