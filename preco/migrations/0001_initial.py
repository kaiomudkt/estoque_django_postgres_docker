# Generated by Django 3.1.2 on 2020-10-31 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dolar', models.DecimalField(decimal_places=2, max_digits=9)),
                ('real', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
    ]