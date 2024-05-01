from django.shortcuts import render
from .models import Names

# Create your views here.
def home(request):
    names = Names.objects.all()
    return render(request, 'index.html', {"names": names})