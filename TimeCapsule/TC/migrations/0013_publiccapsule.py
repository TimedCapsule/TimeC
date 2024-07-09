# Generated by Django 4.2.2 on 2024-07-02 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TC', '0012_alter_timecapsule_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicCapsule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('contributers', models.ManyToManyField(to='TC.timecapsule')),
            ],
        ),
    ]