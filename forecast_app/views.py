from django.shortcuts import render


# Create your views here.
def homepage(request):
    # Create response render
    response = render(request, 'forecast_app/home.html')
    return response
