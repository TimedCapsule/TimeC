# Generated by Django 4.2.2 on 2024-06-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TC', '0008_timecapsule_force_open_pass'),
    ]

    operations = [
        migrations.AddField(
            model_name='timecapsule',
            name='is_force_opened',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]