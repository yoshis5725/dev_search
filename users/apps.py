from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self):
        import users.signals
        # This imports the signals module when the app is ready.
        # The signals module contains the signal handlers that are connected to the signals.
        # This ensures that the signal handlers are registered and ready to handle signals.
