# Generated by Django 4.1.7 on 2023-03-13 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connect', '0008_gitrepository_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gitissue',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
