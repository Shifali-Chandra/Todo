from django.apps import AppConfig


class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'


class UserProfileConfig(AppConfig):
    name = 'userprofile'

    # add this function
    def ready(self):
        from . import signals

# users/__init__.py 
default_app_config = 'users.apps.UsersConfig'