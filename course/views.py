from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
import os

APP = "course"


def index(request):
    return render(request, f"{APP}/index.html")


def about(request):
    return render(request, f"{APP}/about-us.html")


def gallery(request):
    return render(request, f"{APP}/gallery.html")


def contact(request):
    return render(request, f"{APP}/contact-us.html")


def blog(request):
    return render(request, f"{APP}/blog.html")


def all_blogs(request):
    return render(request, f"{APP}/all-blogs.html")


def batch_time_table(request, batch_name: str):
    # TODO: Check if batch name is just filename and not other path. can be vulnerable to attacks
    table_path = os.path.join("course", "utils", "batch_data", f"{batch_name}.json")
    tables_data = None
    try:
        with open(table_path) as f:
            tables_data = json.load(f)
    except Exception as e:
        pass
    if tables_data is None:
        return redirect("/")
    return render(request, f"{APP}/batch-time-table.html", {"tables_data": tables_data})
