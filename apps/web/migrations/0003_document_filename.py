# Generated by Django 2.0.3 on 2018-04-17 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20180417_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='filename',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
