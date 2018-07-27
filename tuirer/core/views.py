from django.shortcuts import render
from django.http import HttpResponse
from core.helpers import print_name, get_character_name
from random import randint
from datetime import *
from tuites.models import Tuite

# Create your views here.
def index(request):
    #return HttpResponse(get_character_name(randint(1,100)))
    # get_character_name(randint(1,100)

    context = {
        'now' : datetime.now(),
        'tuites' : Tuite.objects.all(),
    }

    return render(request, 'home.html', context)
