# Generated by Django 5.0.1 on 2024-04-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_sharingfood'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharingfood',
            name='foodtype',
            field=models.CharField(blank=True, choices=[('RAW', 'raw'), ('COOKED', 'cooked'), ('PACKED', 'packed')], default='COOKED', max_length=9, null=True),
        ),
    ]
