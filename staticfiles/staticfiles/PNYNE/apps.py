from django.apps import AppConfig


class PnyneConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PNYNE'

    def ready(self):
        import PNYNE.signals