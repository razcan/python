from django.shortcuts import render 
# #render_to_response
from django.http import HttpResponse
import mysql.connector
from mysql.connector import errorcode
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
     mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="vasilica",
        database="RZC"
        )

     mycursor = mydb.cursor()   
     mycursor.execute("SELECT * FROM Logs")
     myresult = mycursor.fetchall()
     print(myresult)
     args = {}
     args['mytext'] = "text"
     return TemplateResponse(request, template_name, args)

def read_data(request):
    text_res = "hello comanda executata"
    print(text_res)
    return render(request,"index.html",{'text_res': text_res})
    
    # # import function to run
    # from path_to_script import function_to_run

    # # call function
    # function_to_run() 

    # # return user to required page
    # return HttpResponseRedirect(reverse(app_name:view_name)