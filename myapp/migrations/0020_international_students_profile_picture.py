# Generated by Django 5.0.7 on 2024-07-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_add_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='international_students',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
