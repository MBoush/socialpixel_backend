# Generated by Django 3.1.5 on 2021-01-16 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210106_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reply_to_comment',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
