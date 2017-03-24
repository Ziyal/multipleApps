from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, "disapearing_ninjas/index.html")

def ninjas(request):
    context = {
    'ninjasColor': 'false'
    }
    return render(request, "disapearing_ninjas/ninjas.html", context)

def color(request, color):
    context = {
    'ninjasColor': 'true',
    'color': color
    }
    return render(request, "disapearing_ninjas/ninjas.html", context)
