from celery import shared_task
from django.utils.timezone import now
from pytz import timezone
from .models import UserProfile

@shared_task
def restar_vidas_por_inactividad():
    chile_tz = timezone('America/Santiago')
    hoy = now().astimezone(chile_tz).date()
    profiles = UserProfile.objects.all()

    for profile in profiles:
        if profile.last_trivia_date < hoy:  
            profile.lives = max(0, profile.lives - 1)  
            profile.save()
