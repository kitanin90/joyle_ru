from django.shortcuts import render
from django.utils import timezone
from .models import *


def post_transport(request):
    transport = Transport.objects.filter()
    return render(request, 'captive/index.html', {})
