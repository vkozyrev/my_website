# Create your views here.
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.core import serializers

from my_website.applications.models import Application

def index(request):
    return HttpResponse("INDEX!")

def listApplications(request):
    return HttpResponse("listApplications!")

def luckyCookieFortune(request):

    luckyCookieApplication = Application.objects.get(applicationName = "Lucky Cookie Fortune")
    return render_to_response('applications/application.html', {'application': luckyCookieApplication})
