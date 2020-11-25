# Generated by Django 3.1.3 on 2020-11-25 10:31

from django.db import migrations
from django.utils.text import slugify


def popular_slug(apps, schema_editor):
    Module = apps.get_model('modulos', 'Module')
    for module in Module.objects.all():
        module.slug = slugify(module.title)
        module.save()


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0002_module_slug'),
    ]

    operations = [
        migrations.RunPython(popular_slug)
    ]
