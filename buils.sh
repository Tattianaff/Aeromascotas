#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

# Ejecutar collectstatic para compilar los archivos estáticos
python manage.py collectstatic --noinput

# Ejecutar migraciones para configurar la base de datos
python manage.py migrate