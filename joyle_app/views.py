from django.shortcuts import render
from django.utils import timezone
from .models import *


def post_transport(request):
    transports = Transport.objects.all()
    return render(request, 'captive/index.html', {'transports': transports})
