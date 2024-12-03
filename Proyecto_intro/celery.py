from celery import Celery

app = Celery('Proyecto_intro')

app.conf.beat_schedule = {
    'restar_vidas_por_inactividad': {
        'task': 'Terry.tasks.restar_vidas_por_inactividad',
        'schedule': crontab(hour=23, minute=59),
    },
}
