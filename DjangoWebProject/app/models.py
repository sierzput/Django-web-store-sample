"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

# Create your models here.
class Item(models.Model):
    """Przedmiot"""
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.CharField(max_length=1000, verbose_name=_('Description'))
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('Price'))
    #image = models.ImageField(verbose_name=_('Price'))

    def __str__(self):
        return self.name + ' (' + str(self.price) + ' zł)'

class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name=_('Quantity'))
    user = models.ForeignKey(User, unique=True)

    def __str__(self):
        return self.item.name + ' (' + str(self.item.price * self.quantity) + ' zł)'