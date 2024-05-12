# Generated by Django 5.0.4 on 2024-05-12 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advocate',
            fields=[
                ('advocate_id', models.IntegerField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('father_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True, null=True)),
                ('tin', models.CharField(max_length=100)),
                ('gst', models.CharField(max_length=30)),
                ('pan', models.CharField(max_length=20)),
                ('hourly_rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='uploaded')),
                ('file_name', models.CharField(blank=True, max_length=20, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('doc_type', models.CharField(blank=True, max_length=20, null=True)),
                ('would_like_to_linkdoc', models.BooleanField()),
                ('case_name', models.CharField(blank=True, max_length=20, null=True)),
                ('term', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('judgement_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('purpose', models.CharField(max_length=50)),
                ('first_party', models.CharField(max_length=50)),
                ('second_party', models.CharField(max_length=50)),
                ('headed_by', models.CharField(max_length=50)),
                ('uploaded_by', models.CharField(max_length=20)),
                ('uploaded_at', models.DateField(auto_now_add=True)),
                ('size', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='team_member',
            fields=[
                ('member_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='case',
            fields=[
                ('case_number', models.IntegerField(primary_key=True, serialize=False)),
                ('case_type', models.CharField(max_length=100)),
                ('court', models.CharField(max_length=50)),
                ('cnr_number', models.BooleanField()),
                ('cnr', models.CharField(max_length=100)),
                ('respondent', models.CharField(max_length=100)),
                ('high_court', models.CharField(max_length=50)),
                ('year', models.DateField()),
                ('appearing_as', models.CharField(max_length=100)),
                ('Petitioner', models.CharField(max_length=100)),
                ('date_of_filling', models.DateField()),
                ('court_hall', models.CharField(max_length=100)),
                ('floor', models.CharField(max_length=50)),
                ('classification', models.CharField(max_length=100)),
                ('tital', models.CharField(max_length=60)),
                ('disc', models.CharField(max_length=100)),
                ('Before_Honble_Judg', models.CharField(max_length=100)),
                ('ref_by', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=50)),
                ('Priority', models.CharField(max_length=100)),
                ('under_act', models.CharField(max_length=50)),
                ('under_section', models.CharField(max_length=50)),
                ('fir_police_station', models.CharField(max_length=50)),
                ('fir_number', models.CharField(max_length=50)),
                ('fir_year', models.DateField()),
                ('affidavit_vakalat', models.BooleanField()),
                ('filed', models.BooleanField()),
                ('affidavit_vakalat_date', models.DateField()),
                ('advocate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handle_units.advocate')),
            ],
        ),
        migrations.CreateModel(
            name='contact_point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('designation', models.CharField(max_length=20)),
                ('advocate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handle_units.advocate')),
            ],
        ),
        migrations.CreateModel(
            name='home_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(max_length=255)),
                ('address_line2', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zip_postal_code', models.CharField(max_length=20)),
                ('advocate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handle_units.advocate')),
            ],
        ),
        migrations.CreateModel(
            name='office_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(max_length=255)),
                ('address_line2', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zip_postal_code', models.CharField(max_length=20)),
                ('advocate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handle_units.advocate')),
            ],
        ),
        migrations.CreateModel(
            name='opponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handle_units.case')),
            ],
        ),
        migrations.CreateModel(
            name='opponent_advocate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handle_units.case')),
            ],
        ),
        migrations.CreateModel(
            name='ToDO',
            fields=[
                ('to_do_id', models.IntegerField(primary_key=True, serialize=False)),
                ('advocate_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('assign_by', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('case_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handle_units.case')),
            ],
        ),
    ]
