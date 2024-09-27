#!/bin/bash

# Создание файлов перевода и их компиляция
django-admin makemessages -l ru
django-admin compilemessages

# Выполнение основной команды запуска
exec "$@"
