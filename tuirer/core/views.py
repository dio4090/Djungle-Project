from django.shortcuts import render
from django.http import HttpResponse
from core.helpers import print_name, get_character_name
from random import randint
from datetime import *

# Create your views here.
def index(request):
    #return HttpResponse(get_character_name(randint(1,100)))
    # get_character_name(randint(1,100)

    context = {
        'now' : datetime.now(),
        'my_name' : 'Diogo',
    }

    return render(request, 'home.html', context)
