# Generated by Django 5.1.4 on 2025-01-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='profile-img/default-img.png', upload_to='media/profile-img/'),
        ),
    ]
