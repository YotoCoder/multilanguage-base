from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    name = models.CharField(_('name'), max_length=50, help_text=_('Enter the name of the product'))
    description = models.TextField(_('description'), blank=True, help_text=_('Enter a description for the product'))
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, help_text=_('Enter the price of the product'))
    stock = models.IntegerField(_('stock'), help_text=_('Enter the amount in stock for the product'))
    image = models.ImageField(_('image'), upload_to='products/', help_text=_('Upload an image for the product'))

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        
    def __str__(self):
        return f'{self.name} - {self.price}'