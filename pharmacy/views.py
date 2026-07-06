from django.shortcuts import render
from .models import Medicine

def home(request):
    medicines = Medicine.objects.all()  # Changed this line
    return render(request, 'pharmacy/home.html', {'medicines': medicines})
