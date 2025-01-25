from django.http import HttpResponse
from django.shortcuts import render


APP = "course"


def index(request):
    return render(request, f"{APP}/index.html")


def about(request):
    return render(request, f"{APP}/about-us.html")


def gallery(request):
    return render(request, f"{APP}/gallery.html")


def contact(request):
    return render(request, f"{APP}/contact-us.html")
