# Generated by Django 5.0.6 on 2024-05-30 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0003_alter_workers_image_alter_workers_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='username',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]