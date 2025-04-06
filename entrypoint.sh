#!/bin/bash

# Создание файлов перевода и их компиляция
django-admin makemessages -l ru
django-admin compilemessages
python manage.py collectstatic --noinput

# Выполнение основной команды запуска
exec "$@"
