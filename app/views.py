"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext, loader
from django.template.loader import render_to_string
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    context = {
             'title': 'Home Page',
             'year': datetime.now().year,
         }
    return HttpResponse(render_to_string('app/index.html', context, request))

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    context = {
          'title': 'Contact',
          'message': 'Your contact page.',
          'year': datetime.now().year,
        }
    return HttpResponse(render_to_string('app/contact.html', context))

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    context = {
                 'title': 'About',
                 'message': 'Your application description page.',
                 'year': datetime.now().year,
             }
    return HttpResponse(render_to_string('app/about.html', context))
