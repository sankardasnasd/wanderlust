# Generated by Django 3.2.24 on 2024-10-21 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_guide_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guide_booking',
            name='price',
        ),
        migrations.AddField(
            model_name='guide_booking',
            name='status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
