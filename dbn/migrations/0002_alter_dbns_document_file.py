# Generated by Django 5.0.2 on 2024-03-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbns',
            name='document_file',
            field=models.FileField(upload_to='dbns/'),
        ),
    ]
