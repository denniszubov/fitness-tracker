# Generated by Django 5.0.3 on 2024-04-10 20:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run', '0002_rename_notes_run_general_notes_remove_run_runner_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='runs', to=settings.AUTH_USER_MODEL),
        ),
    ]
