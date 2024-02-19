from django.shortcuts import render

from . import models


def home(request):

    pro = models.product.objects.all()
    return render(request, 'home.html', {'pro': pro})


# Create your views here.
