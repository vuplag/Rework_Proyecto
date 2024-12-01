from django.apps import AppConfig

class TerryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Terry'

    def ready(self):
        import Terry.signals  # Asegúrate de que las señales se carguen
