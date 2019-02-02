# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'newApp/index.html')

def other(request):
    return HttpResponse("hit the back button")

def odell(request):
    return render(request, 'newApp/odell.html')