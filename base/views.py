from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home (request):
    item_list = ['Python', 'Django', 'JavaScript', 'SQL', 'CSS3', 'Scripts', 'Heroku']
    rand_item_list = random.sample(item_list, 7)

    context = {'item_list': rand_item_list}
    return render(request, 'base/home.html', context)