from django.shortcuts import render
from django.conf import settings

# Create your views here.

def cert_info(request):
    print(settings.BASE_DIR)
    return render(request, 'cert_info.html')

def output(request):
    data = "test data"
    return render(request, 'cert_info.html', {'data':data})
