from django.shortcuts import render


def index(request):
    """A vies that sidplays the index page"""
    return render(request, 'index.html')
