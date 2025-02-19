# Generated by Django 5.0.4 on 2024-07-02 16:24

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_dataset', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='KomunikasiManajemen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModelPlanning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=100)),
                ('deskripsi_model', models.TextField(blank=True, max_length=100, null=True)),
                ('tujuan_model', models.TextField(blank=True, max_length=100, null=True)),
                ('nama_algoritma', models.CharField(blank=True, max_length=100, null=True)),
                ('kebutuhan_data', models.TextField(blank=True, max_length=100, null=True)),
                ('metodologi_pengujian', models.TextField(blank=True, max_length=100, null=True)),
                ('metode_pengukuran', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(blank=True, max_length=100, null=True)),
                ('project_name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('algorithm', models.CharField(blank=True, max_length=50, null=True)),
                ('output', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('data_type', models.CharField(max_length=255)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='input_data.dataset')),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datasets', to='input_data.project'),
        ),
        migrations.CreateModel(
            name='Proses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_aktivitas', models.Field()),
                ('deskripsi_aktivitas', models.TextField()),
                ('result_file', models.FileField(upload_to='activity_results/')),
                ('status', models.CharField(choices=[('Belum Selesai', 'Belum Selesai'), ('Sedang Proses', 'Sedang Proses'), ('Selesai', 'Selesai')], default='Belum Selesai', max_length=20)),
                ('dataset_yang_dipakai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input_data.dataset')),
            ],
        ),
        migrations.CreateModel(
            name='RefiningPlanning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('refining_goal', models.TextField()),
                ('refining_strategy', models.CharField(max_length=100)),
                ('additional_data', models.TextField()),
                ('evaluation_methodology', models.TextField()),
                ('measurement_method', models.TextField()),
                ('evaluasi_model_awal', models.TextField(blank=True, max_length=100, null=True)),
                ('model_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refinings', to='input_data.modelplanning')),
            ],
        ),
        migrations.CreateModel(
            name='RefiningResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refining_result', models.FileField(upload_to='refining_results/')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input_data.modelplanning')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input_data.dataset')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input_data.project')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingTestingResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_result', models.FileField(upload_to='training_results/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv', 'pickle'], message='Only CSV and Pickle files are allowed for training results.')])),
                ('testing_result', models.FileField(upload_to='testing_results/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv', 'pickle'], message='Only CSV and Pickle files are allowed for testing results.')])),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input_data.modelplanning')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input_data.dataset')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input_data.project')),
            ],
        ),
    ]
