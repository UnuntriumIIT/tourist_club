# Generated by Django 4.1.1 on 2022-09-14 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_site', '0002_article_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_src',
            field=models.URLField(),
        ),
    ]
