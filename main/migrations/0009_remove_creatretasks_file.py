# Generated by Django 3.0 on 2021-07-14 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_creatretasks_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creatretasks',
            name='file',
        ),
    ]