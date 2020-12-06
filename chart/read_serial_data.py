

import serial
import time
import mysql.connector
from mysql.connector import errorcode
from datetime import date
from django.http import HttpResponse
from django.shortcuts import render 
from django.db import models
#from chart.models import *
from models import Info

class MyAppConfig():
    today = date.today()
    z1baudrate = 9600
    z1port = '/dev/ttyUSB0'  # set the correct port before run it

    z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
    z1serial.timeout = 20 # set read timeout

    z1serial.flushInput()
    z1serial.flushOutput()

    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="vasilica",
        database="RZC"
        )
 
    mycursor = mydb.cursor()   

    if z1serial.is_open:
        while True:
            # info = Info()
            # info.distance = '999'
            # info.time = '2020-12-04 01:56:06.000000'
            # info.save()
            #info_instance = Info.objects.create(distance='999',time='2020-12-04 01:56:06.000000')
            data_raw = z1serial.readline()
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            sql = "INSERT INTO chart_info (distance, time) VALUES (%s, %s)"
            val = (data_raw,timestamp)
            #print(data_raw)
            mycursor.execute(sql, val)
            mydb.commit()


#print (z1serial.is_open)  # True for opened
