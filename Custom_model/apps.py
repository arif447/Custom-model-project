from django.apps import AppConfig


class CustomModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Custom_model'
