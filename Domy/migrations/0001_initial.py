# Generated by Django 2.1.1 on 2023-02-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kogo', models.CharField(max_length=128)),
                ('opis', models.CharField(max_length=500)),
            ],
        ),
    ]
