# Generated by Django 5.0.4 on 2024-07-03 02:45

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_data', '0002_dataprojek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refiningresult',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input_data.proses'),
        ),
        migrations.AlterField(
            model_name='refiningresult',
            name='refining_result',
            field=models.FileField(upload_to='refining_results/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv', 'pickle'], message='Only CSV and Pickle files are allowed for refining results.')]),
        ),
        migrations.AlterField(
            model_name='trainingtestingresult',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input_data.proses'),
        ),
    ]
