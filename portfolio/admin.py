from django.contrib import admin
from .models import Project
from .models import Resume
from .models import About

# Register your models here.

admin.site.register(Project)  # Register the Project model with the admin site
admin.site.register(Resume)  # Register the Resume model with the admin site
admin.site.register(About)  # Register the AboutDetails model with the admin site
