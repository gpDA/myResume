# Generated by Django 2.1 on 2018-08-16 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0006_posttagen_posttagko'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcommenten',
            old_name='project',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='postcommentko',
            old_name='project',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='posttagen',
            old_name='project',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='posttagko',
            old_name='project',
            new_name='post',
        ),
        migrations.RemoveField(
            model_name='posten',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='postko',
            name='tag',
        ),
    ]
