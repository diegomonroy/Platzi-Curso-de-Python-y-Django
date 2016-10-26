from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

from .models import Product

def hello_world(request):
#     return render(request, 'index.html')
    product = Product.objects.order_by('id')
    template = loader.get_template('index.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))