from django import template
from django.shortcuts import render, redirect
from django.db.models import Sum, Count, Q
from services import models
import uuid, socket 

register = template.Library()

@register.filter(name='school')
def school_details(request):
    data      = models.SchoolProfile.objects.filter(status = True)
    return data

@register.filter(name='str2url')
def string_to_url_convert(data):
    #use in view: category = cat.replace('-', ' ')
    # use in html: text|str2url
    data = str(data)    
    return data.replace(' ', '-') 

@register.filter(name='replace')
def replace_load(obj):
    rep = obj.replace("%20"," ")
    return rep
