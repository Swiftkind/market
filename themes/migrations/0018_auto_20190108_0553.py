# Generated by Django 2.1.5 on 2019-01-08 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0017_auto_20190108_0312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='theme',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.RemoveField(
            model_name='screenshot',
            name='theme',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='browser',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='category',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='owners',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='thumbnail',
            name='theme',
        ),
        migrations.DeleteModel(
            name='Browser',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Screenshot',
        ),
        migrations.DeleteModel(
            name='Theme',
        ),
        migrations.DeleteModel(
            name='Thumbnail',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
