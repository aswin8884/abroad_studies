# Generated by Django 5.0.7 on 2024-07-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_rename_image_add_universites_image_main_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_course',
            name='application_link',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
