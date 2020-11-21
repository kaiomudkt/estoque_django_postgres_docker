#!/bin/bash

echo "Aguardando banco de dados terminar a inicializacao"
sleep 3

echo "Making migrations"
python manage.py makemigrations

chown -R $USER:$USER .

python manage.py migrate

echo "Creating super user"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root', 'root', 'root')" | python manage.py shell

echo "Migrating triggers"
cat trigger.sql | python manage.py dbshell

echo "Running server!"
python manage.py runserver 0.0.0.0:8080
