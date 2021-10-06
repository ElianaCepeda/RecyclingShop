from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    salida = "<html>"
    salida = salida + "<body>"
    salida = salida + "<h1>Bienvenido al modulo de registro de RecyclingShop</h1>"
    salida = salida + "<form>"
    salida = salida + "<p>Diligencie sus usuario: <input></input></p>"
    salida = salida + "<p>Diligencie sus password: <input /></p>"
    salida = salida + "<p><input type='submit'></p>"
    salida = salida + "</form>"
    salida = salida + "</body>"
    salida = salida + "</html>"
    return HttpResponse(salida)

# Create your views here.
