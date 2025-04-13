from .models import Resume
from django.core.cache import cache


def resume_context(request):
    # Cache the resume for 1 hour (or longer)
    resume = cache.get("resume_data")
    if not resume:
        resume = Resume.objects.first()
        cache.set("resume_data", resume, 60 * 60)
    return {"resume": resume}
