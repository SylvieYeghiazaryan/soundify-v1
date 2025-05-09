from django.apps import AppConfig

class MusicConfig(AppConfig):
    """
    Configuration class for the 'music' Django app.

    Attributes:
        default_auto_field (str): Specifies the default type for auto-created primary keys.
        name (str): The full Python path to the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'music'
