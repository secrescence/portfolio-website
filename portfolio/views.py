from django.shortcuts import render
from .models import Project
from .models import About
import markdown

# Create your views here.


def home(request):
    return render(request, "portfolio/home.html")


def about(request):
    return render(request, "portfolio/about.html")


def projects(request):
    return render(request, "portfolio/projects.html")


def projects(request):
    projects_list = Project.objects.all()
    return render(
        request, "portfolio/projects.html", {"projects": projects_list}
    )  # fetch all projects from the database and pass them to the template


def about(request):
    about = About.objects.first()
    return render(
        request,
        "portfolio/about.html",
        {
            "what_i_do": markdown.markdown(about.what_i_do),
            "core_skills": markdown.markdown(about.core_skills),
        },
    )
