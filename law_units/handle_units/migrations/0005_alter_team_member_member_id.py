# Generated by Django 5.0.4 on 2024-05-05 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle_units', '0004_remove_team_member_cost_per_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_member',
            name='member_id',
            field=models.IntegerField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
