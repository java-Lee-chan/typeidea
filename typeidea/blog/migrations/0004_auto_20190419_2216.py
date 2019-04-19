# Generated by Django 2.2 on 2019-04-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_content_html'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='标签'),
        ),
    ]
