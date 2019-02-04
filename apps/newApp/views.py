# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from models import *

# Create your views here.

def index(request):
    return render(request, 'newApp/index.html')

def other(request):
    return HttpResponse("hit the back button")

def addItem(request):
    return render(request, "newApp/addItem.html")

def dbAddItem(request):
    print 'omg'
    print request.POST
    x = Item.objects.create(name = request.POST['name'], description = request.POST['description'], color = request.POST['color'], img = request.POST['img'])
    print x
    return redirect('/display')

def displayItems(request):
    context = {
        "jay": "silent bob",
        "items": Item.objects.all(),
    }
    return render(request, 'newApp/displayItems.html', context)

def destroy(request, item_id):
    print "destroying"
    print item_id

    x = Item.objects.get(id= item_id)
    x.delete()
    return redirect('/display')


def odell(request):
    return render(request, 'newApp/odell.html')