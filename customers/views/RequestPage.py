from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from customers.forms import RequestForm

def RequestPage(request):

    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            id = form.instance.id          
            context = {
                'form': form,
                'message': 'Request submitted successfully!',
                'req_id': id,
            }
            return render(request, 'requestPage.html', context)
        else:
            context = {
                'form': form,
            }
            return render(request, 'requestPage.html', context)

    template = loader.get_template('requestPage.html')
    context = {}
    context["form"] = RequestForm()
    return render(request, 'requestPage.html', context)
