# Generated by Django 3.2.7 on 2021-12-13 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20211213_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='author',
        ),
    ]