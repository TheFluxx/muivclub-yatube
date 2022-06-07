# Generated by Django 2.2.6 on 2021-01-12 11:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Здесь писать комментарий',
                                          verbose_name='Текст комментария')),
                ('created', models.DateTimeField(
                    auto_now_add=True,
                    help_text='Здесь укажите дату публикации',
                    verbose_name='date published')),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='comments', to='posts.Post')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
