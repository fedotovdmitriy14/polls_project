# Generated by Django 3.2.3 on 2021-08-14 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_alter_choice_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='poll_name',
            new_name='poll_id',
        ),
    ]
