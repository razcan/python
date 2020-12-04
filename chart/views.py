from django.shortcuts import render 
# #render_to_response
from django.http import HttpResponse
import mysql.connector
from mysql.connector import errorcode
from django.db import models
from chart.models import *

# from django.template import loader

# def index(request):
#     return render(request,'index.html'):


from django.template.response import TemplateResponse

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
     
     print(labels)
     print(data)

     return TemplateResponse(request, template_name, {
        "myresult" : myresult,
        "labels" : labels,
        "data": data,
                                                     })

def read_data(request):
    text_res = "hello comanda executata"
    print(text_res)
    return render(request,"index.html",{'text_res': text_res})