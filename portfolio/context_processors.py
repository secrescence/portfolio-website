from .models import Resume


def resume_context(request):
    return {"resume": Resume.objects.first()}
