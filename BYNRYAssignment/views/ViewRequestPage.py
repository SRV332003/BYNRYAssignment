from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def ViewRequestPage(request):
    template = loader.get_template('viewPage.html')
    return HttpResponse(template.render({}, request))
