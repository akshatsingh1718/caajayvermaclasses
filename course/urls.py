from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about-us", views.about, name="about"),
    path("gallery", views.gallery, name="gallery"),
    path("contact-us", views.contact, name="contact"),
    path("blogs", views.all_blogs, name="all_blogs"),
    path("blogs/<str:blog_name>", views.blog, name="blog"),
    path("batch/<str:batch_name>", views.batch_time_table, name="batch_time_table"),
]
