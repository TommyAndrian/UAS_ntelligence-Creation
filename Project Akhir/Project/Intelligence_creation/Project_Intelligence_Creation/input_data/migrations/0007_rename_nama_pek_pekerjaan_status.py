# Generated by Django 5.0.4 on 2024-07-03 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('input_data', '0006_pekerjaan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pekerjaan',
            old_name='nama_pek',
            new_name='status',
        ),
    ]
