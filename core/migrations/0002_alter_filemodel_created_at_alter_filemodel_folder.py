# Generated by Django 4.1.7 on 2023-03-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='folder',
            field=models.FileField(upload_to=' %m/%Y/folders/'),
        ),
    ]
