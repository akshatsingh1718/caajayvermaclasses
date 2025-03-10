from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
import os

APP = "course"
ALLOWED_COURSES = [
    "ca-foundation.json",
    "ca-inter-group2.json",
    "cma-foundation.json",
    "cseet.json",
    "cs-professional.json",
    "ca-inter-group1.json",
    "cma-final.json",
    "cma-intermediate.json",
    "cs-executive.json",
]

BLOGS = {
    "top-3-courses-after-12th-commerce": {
        "title": "Top 3 Courses After 12th Commerce",
        "author": "Mr. Ajay Verma",
        "image_url": "assets/images/landing-banner-1.png",
        "url": "top-3-courses-after-12th-commerce",
    }
}


def index(request):
    return render(request, f"{APP}/index.html")


def about(request):
    return render(request, f"{APP}/about-us.html")


def gallery(request):
    return render(request, f"{APP}/gallery.html")


def contact(request):
    return render(request, f"{APP}/contact-us.html")


def blog(request, blog_name: str):
    if blog_name not in BLOGS:
        return redirect("/")

    return render(request, f"{APP}/blogs/{blog_name}.html")


def all_blogs(request):
    return render(request, f"{APP}/all-blogs.html", {"blogs": BLOGS})


def batch_time_table(request, batch_name: str):

    # TODO: Check if batch name is just filename and not other path. can be vulnerable to attacks
    filename = f"{batch_name}.json"
    if filename not in ALLOWED_COURSES:
        return redirect("/")
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
