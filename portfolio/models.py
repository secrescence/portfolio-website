from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="project_images/", blank=True, null=True)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class Resume(models.Model):
    name = models.CharField(max_length=100, default="My Resume")
    file_url = models.URLField(
        max_length=500,
        help_text="Link to your resume (e.g., Google Drive, GitHub, etc.)",
    )

    def __str__(self):
        return self.name
