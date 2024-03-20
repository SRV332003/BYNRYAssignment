from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from ..models import Request

def ViewRequestPage(request):

    try:
        query = request.GET["query"]
        if query != "":
            query = request.GET["query"]
            try:
                req = Request.objects.get(id=int(query))
            except:
                req = ""
            context = {
                'req': req,
                'searchform': False,
            }
            template = loader.get_template('viewPage.html')
            return HttpResponse(template.render(context, request))
            
    except Exception as e:
        print(e)
        

    template = loader.get_template('viewPage.html')

    return render(request, 'viewPage.html',{"req": -1})