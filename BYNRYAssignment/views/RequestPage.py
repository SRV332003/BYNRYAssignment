from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def RequestPage(request):
    template = loader.get_template('requestPage.html')

    return HttpResponse(template.render({}, request))
