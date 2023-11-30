from django.shortcuts import render
from django.http import HttpResponse

from .models import project, project_language, project_language_mapping

def index(request):

    context = {
        }

    index_render = render(request,'templates/index.html', context)    
    return index_render
