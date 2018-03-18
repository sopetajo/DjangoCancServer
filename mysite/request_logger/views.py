# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Request_log
from django.utils import timezone

def index(request):
    content = request.META['QUERY_STRING']
    newReq = Request_log.objects.create(log_content = content, log_date = timezone.now())
    return HttpResponse("OK " + content)


# Create your views here.
