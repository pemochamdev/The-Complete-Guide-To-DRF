# Generated by Django 4.2.8 on 2023-12-27 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_article_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
