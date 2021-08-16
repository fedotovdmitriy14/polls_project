# Generated by Django 3.2.3 on 2021-08-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_rename_poll_name_question_poll_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('TEXT', 'TEXT'), ('SINGLE', 'SINGLE'), ('MULTI', 'MULTI')], default='TEXT', max_length=6),
        ),
    ]