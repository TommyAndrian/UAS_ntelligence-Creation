# Generated by Django 5.0.4 on 2024-07-03 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('input_data', '0004_dataprojek_id_proyek_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataprojek',
            name='id_proyek',
        ),
    ]
