from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="portfolio"),  # Home page view
    path("about/", views.about, name="about"),  # About page view
    path("projects/", views.projects, name="projects"),  # Projects page view
]
