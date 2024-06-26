# Generated by Django 5.0.3 on 2024-04-06 02:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='run',
            old_name='notes',
            new_name='general_notes',
        ),
        migrations.RemoveField(
            model_name='run',
            name='runner',
        ),
        migrations.AddField(
            model_name='run',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='does', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
