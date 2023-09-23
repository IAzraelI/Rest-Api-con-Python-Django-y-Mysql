from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Aquí podemos enviar archivos html, lo que se va a mostrar en el cliente o al
# navegador.


def hello(request):
    return HttpResponse("<h2>Hello World</h2>")


def about(request):
    return HttpResponse("About")
