# Generated by Django 5.0.7 on 2024-07-20 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_add_course_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_course',
            name='c_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
