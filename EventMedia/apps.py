from django.apps import AppConfig

class EventMediaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EventMedia'

    def ready(self):
        import EventMedia.signals
