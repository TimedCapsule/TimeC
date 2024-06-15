# Generated by Django 5.0.3 on 2024-06-15 07:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeCapsule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('private', 'private'), ('public', 'public')], max_length=20)),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('future_date', models.DateTimeField()),
                ('text', models.TextField(max_length=500)),
                ('image1', models.ImageField(upload_to='media/images')),
                ('image2', models.ImageField(upload_to='media/images')),
                ('video1', models.CharField(max_length=300)),
                ('video2', models.CharField(max_length=300)),
                ('collaborators', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_users', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
