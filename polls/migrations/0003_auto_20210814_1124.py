# Generated by Django 3.2.3 on 2021-08-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_polls_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='polls',
            name='description',
            field=models.TextField(default='poll'),
        ),
        migrations.AddField(
            model_name='polls',
            name='end_date',
            field=models.DateField(default='2021-12-12'),
        ),
    ]