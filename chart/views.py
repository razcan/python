# from django.shortcuts import render 
# #render_to_response
from django.http import HttpResponse
# from django.template import loader

# def index(request):
#     return render(request,'index.html'):


from django.template.response import TemplateResponse

def index(request, template_name="index.html"):
    args = {}
    text = "hello world"
    args['mytext'] = text
    return TemplateResponse(request, template_name, args)
