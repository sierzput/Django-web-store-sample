"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.utils.translation import ugettext as _
from app.models import Item

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':_('Home Page'),
            'year':datetime.now().year,
        }
    )

def itemsList(request):
    """Renders the list of items."""
    assert isinstance(request, HttpRequest)
    items = Item.objects.all()
    return render(
        request,
        'app/itemsList.html',
        {
            'title':_('Items list'),
            'items':items,
        }
    )

def itemDetails(request, id):
    """Renders the item details page."""
    assert isinstance(request, HttpRequest)
    item = Item.objects.get(pk = id)
    return render(
        request,
        'app/itemDetails.html',
        {
            'title':item.name,
            'item':item,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':_('Contact'),
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':_('About'),
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
