from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^items/$', views.itemsList, name='items'),
    url(r'^items/(?P<id>[0-9]+)/$', views.itemDetails, name='item details'),
    url(r'^contact$', views.contact, name='contact'),
]