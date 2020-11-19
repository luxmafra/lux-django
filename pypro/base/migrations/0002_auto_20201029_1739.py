# Generated by Django 3.1.2 on 2020-10-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all'
                                                               ' permissions without explicitly assigning '
                                                               'them.', verbose_name='superuser status'),
        ),
    ]
