#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

############################  Django Runserver Commandline ############################## 
# (LOCAL) DJANGO_SETTINGS_MODULE=configs.environments.local ./manage.py runserver 0:8000
# (DEV)   DJANGO_SETTINGS_MODULE=configs.environments.dev ./manage.py runserver 0:8000
# (PROD)  DJANGO_SETTINGS_MODULE=configs.environments.prod ./manage.py runserver 0:8000
#########################################################################################

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings.local')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
