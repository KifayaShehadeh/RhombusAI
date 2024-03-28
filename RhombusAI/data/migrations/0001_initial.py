# Generated by Django 4.1.7 on 2024-03-27 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file_name', models.CharField(max_length=255)),
                ('processed_at', models.DateTimeField(blank=True, null=True)),
                ('original_file', models.FileField(upload_to='datasets/')),
            ],
        ),
        migrations.CreateModel(
            name='ColumnType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=255)),
                ('original_type', models.CharField(max_length=50)),
                ('inferred_type', models.CharField(max_length=50)),
                ('user_modified_type', models.CharField(blank=True, max_length=50, null=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='column_types', to='data.dataset')),
            ],
        ),
    ]
