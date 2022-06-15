from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view to allow the user to view their bag """

    return render(request, 'bag/bag.html')
