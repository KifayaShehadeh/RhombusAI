# Generated by Django 4.1.7 on 2024-04-01 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_dataset_processed_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='processed_file_pkl',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]