# Generated by Django 4.2.7 on 2023-11-18 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='form',
            options={'verbose_name': 'Форма отправки', 'verbose_name_plural': 'Формы отправки'},
        ),
        migrations.RenameField(
            model_name='form',
            old_name='team',
            new_name='factory',
        ),
        migrations.AddField(
            model_name='form',
            name='status',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
