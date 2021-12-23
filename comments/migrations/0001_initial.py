# Generated by Django 3.0 on 2021-06-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_num', models.CharField(blank=True, max_length=30, verbose_name='Номер задачи')),
                ('date_answer', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('owner_name', models.CharField(blank=True, max_length=30, verbose_name='Имя пользователя')),
                ('owner_id', models.CharField(blank=True, max_length=3, verbose_name='ID пользователя')),
                ('slug_task_com', models.CharField(blank=True, max_length=255, verbose_name='slug')),
                ('answer_text', models.TextField(blank=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Комментарии',
                'verbose_name_plural': 'Комментарии',
                'db_table': 'comments',
            },
        ),
    ]
