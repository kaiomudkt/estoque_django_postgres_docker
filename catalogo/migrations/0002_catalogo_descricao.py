# Generated by Django 3.1.2 on 2020-10-31 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogo',
            name='descricao',
            field=models.TextField(default='vazio'),
            preserve_default=False,
        ),
    ]
