import json
from venv import logger

import requests
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def products(request):
    quotes = requests.get('http://127.0.0.1:8000/quotes')
    quotes = quotes.json()
    return render(request, 'home.html', {'quotes':quotes})

def like(request, pk):
    req = requests.get('http://127.0.0.1:1234/quotes/' + str(pk) + '/like')
    print(req)
    messages.info(request, json.loads(req.content))
    return redirect('/')
