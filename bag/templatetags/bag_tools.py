from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calaculates subtotal in instances of more than 1 item wanted """
    return price * quantity
