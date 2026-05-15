from django.shortcuts import render


# Homepage view
# Renders the main homepage template
def home(request):
    return render(request, 'products/home.html')