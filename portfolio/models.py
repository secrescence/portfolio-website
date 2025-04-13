from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField("image", blank=True, null=True)
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


class About(models.Model):
    what_i_do = models.TextField(
        verbose_name="What I Do",
        help_text="Describe what you do and your professionals background. Use markdown for formatting.",
        null=True,
        blank=True,
    )
    core_skills = models.TextField(
        verbose_name="Core Skills",
        help_text="List your core skills and areas of expertise. Use markdown for formatting.",
        null=True,
        blank=True,
    )

    def __str__(self):
        return "About and Core Skills"
