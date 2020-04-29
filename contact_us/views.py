from django.shortcuts import render


# Create your views here.
def contact_us(request):
    """ A view that displays the contact us page """
    return render(request, "contact_us.html")