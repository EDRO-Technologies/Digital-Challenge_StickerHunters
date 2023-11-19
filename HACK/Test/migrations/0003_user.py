# Generated by Django 4.2.5 on 2023-11-18 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_alter_form_options_rename_team_form_factory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('password', models.TextField()),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
