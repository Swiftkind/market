# Generated by Django 2.1.4 on 2019-01-04 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0003_auto_20190104_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='themes',
            name='review',
            field=models.ManyToManyField(blank=True, to='themes.Review'),
        ),
    ]
