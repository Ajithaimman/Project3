# Generated by Django 5.0.1 on 2024-05-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_alter_sharingfood_foodtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodSharing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('foodname', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('foodtype', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SharingFood',
        ),
    ]
