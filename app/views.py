"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.utils.translation import ugettext as _
from app.models import Item, CartItem
from app.CartListItem import CartListItem
from functools import reduce

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Strona główna',
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
            'title':'Lista przedmiotów',
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

def addToCart(request, id):
    """Adding item to cart."""
    assert isinstance(request, HttpRequest)
    if not request.user.is_authenticated:
        return redirect('login')
    item = Item.objects.get(pk = id)
    cartItem = CartItem.objects.filter(user=request.user, item_id=item.id).first()
    if cartItem!=None:
        cartItem.quantity+=1
    else:
        cartItem = CartItem.objects.create(item=item, quantity=1, user=request.user)
    cartItem.save()
    request.toast = 'Dodano do koszyka'
    return redirect('cart items')

def removeFromCart(request, id):
    """Removing item from cart."""
    assert isinstance(request, HttpRequest)
    if not request.user.is_authenticated:
        return redirect('login')
    cartItem = CartItem.objects.filter(user=request.user, item_id=id).first()
    if cartItem != None:
        cartItem.quantity-=1
        cartItem.save()
        if cartItem.quantity <= 0:
            cartItem.delete()
        request.toast = 'Usunięto z koszyka'
    return redirect(
        request.META['HTTP_REFERER']
    )

def cartItems(request):
    """Renders items from user cart."""
    assert isinstance(request, HttpRequest)
    if not request.user.is_authenticated:
        return redirect('login')
    cartItems = CartItem.objects.filter(user=request.user)
    cartItems = list(map(lambda item: CartListItem(item), cartItems))
    total = reduce(lambda a, b: a + b, map(lambda item: item.total, cartItems), 0)
    return render(
        request,
        'app/cart.html',
        {
            'title':'Koszyk',
            'cartItems':cartItems,
            'total':total
        }
    )

def clearCart(request):
    """Delete all items from cart."""
    assert isinstance(request, HttpRequest)
    if not request.user.is_authenticated:
        return redirect('login')
    CartItem.objects.filter(user=request.user).delete()
    return redirect(
        request.META['HTTP_REFERER']
    )

def buy(request):
    """Buying items."""
    assert isinstance(request, HttpRequest)
    if not request.user.is_authenticated:
        return redirect('login')

    CartItem.objects.filter(user=request.user).delete()
    return redirect(
        request.META['HTTP_REFERER']
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Kontakt',
            'message':'Skontaktuj się z nami.',
            'year':datetime.now().year,
        }
    )

