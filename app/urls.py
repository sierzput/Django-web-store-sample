from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^items/$', views.itemsList, name='items'),
    url(r'^items/(?P<id>[0-9]+)/$', views.itemDetails, name='item details'),
    url(r'^addToCart/(?P<id>[0-9]+)/$', views.addToCart, name='add to cart'),
    url(r'^removeFromCart/(?P<id>[0-9]+)/$', views.removeFromCart, name='remove from cart'),
    url(r'^cart/$', views.cartItems, name='cart items'),
    url(r'^clearCart/$', views.clearCart, name='clear cart'),
    url(r'^buy/$', views.buy, name='buy'),
    url(r'^contact$', views.contact, name='contact'),
]