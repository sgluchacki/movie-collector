# Generated by Django 3.0.5 on 2020-06-21 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(default='Django', max_length=100),
            preserve_default=False,
        ),
    ]