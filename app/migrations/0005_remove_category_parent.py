# Generated by Django 4.2.5 on 2023-10-10 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]