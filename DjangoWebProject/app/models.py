"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nazwa')
    description = models.CharField(max_length=1000, verbose_name='Opis produktu')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Cena')

    def __str__(self):
        return self.name + ' (' + str(self.price) + ' zł)'

    class Meta:
        verbose_name = "Przedmiot"
        verbose_name_plural = "Przedmioty"

class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name=_('Ilość'))
    user = models.ForeignKey(User)

    def __str__(self):
        return self.item.name + ' (' + str(self.item.price * self.quantity) + ' zł)'
    
    class Meta:
        verbose_name = "Przedmiot w koszyku klienta"
        verbose_name_plural = "Przedmioty w koszyku klienta"