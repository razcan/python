from django.shortcuts import render 
#render_to_response
from django.http import HttpResponse
from django.template import loader

def index(request):
    # View code here...
    return render(request,'index.html')
    # return render(request, 'chart/index.html', {
    #    'latest_question_list': '1',
    #     }
    #               )