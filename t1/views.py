from django.shortcuts import render
import requests

# Create your views here.
# https://www.youtube.com/watch?v=ERMRVORGvZM

def button(request):
    return render(request, 'home.html')

def output(request):
    data = requests.get('https://reqres.in/api/users')
    print(data.text)
    data = data.text
    return render(request, 'home.html', {'data':data})
