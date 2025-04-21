from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # Automatically register custom filters
        autodiscover_modules('custom_filters')
