# Generated by Django 4.2.1 on 2023-10-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produs', '0004_servicii_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicii',
            name='servicii',
            field=models.ImageField(null=True, upload_to='servicii/'),
        ),
    ]