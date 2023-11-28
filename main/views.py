from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context = {
        }

    index_render = render(request,'templates/index.html', context)    
    return index_render
