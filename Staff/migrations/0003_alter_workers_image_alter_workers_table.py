# Generated by Django 5.0.6 on 2024-05-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0002_alter_workers_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='image',
            field=models.ImageField(default='default_image.png', upload_to='profile_image/'),
        ),
        migrations.AlterModelTable(
            name='workers',
            table=None,
        ),
    ]
