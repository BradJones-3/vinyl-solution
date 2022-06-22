from django.shortcuts import render


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "HELP! I Need Some Items! Your Bag Is Empty")