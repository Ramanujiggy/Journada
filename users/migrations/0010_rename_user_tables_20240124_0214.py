# Generated by Django 5.0 on 2024-01-24 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_is_active_user_is_staff_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.RenameModel('User', 'Profile'),
        migrations.RenameModel('Session', 'GrappleEntry')
    ]
