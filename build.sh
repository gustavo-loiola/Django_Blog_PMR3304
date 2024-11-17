#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

# Criar e aplicar migrações
python manage.py makemigrations
python manage.py migrate

# Define DJANGO_SETTINGS_MODULE para evitar erro de configuração
export DJANGO_SETTINGS_MODULE="blogdinamico.settings"

# create superuser if missing
python << EOF
import os
from django import setup
from django.contrib.auth import get_user_model

# Inicializa o Django para carregar as configurações corretamente
setup()

User = get_user_model()
username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

# Cria o superusuário se ainda não existir
if username and email and password:
    if not User.objects.filter(username=username).exists():
        print("Criando superusuário...")
        User.objects.create_superuser(username, email, password)
    else:
        print("Superusuário já existe.")
else:
    print("Variáveis de ambiente do superusuário não configuradas corretamente.")
EOF