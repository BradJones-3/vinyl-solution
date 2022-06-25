from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "HELP! I Need Some Items! Your Bag Is Empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_live_51KUDkJGqe9QmhagcSovqJmWseyb5k37iQtnA2mKP00Czy3Oj8ZGRzZJpc8HE1Z0Mskts6oNQbczQZ7XZf3TbgtiC00zECeKB63',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)