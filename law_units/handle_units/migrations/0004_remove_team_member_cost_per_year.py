# Generated by Django 5.0.4 on 2024-05-05 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handle_units', '0003_remove_team_member_id_alter_team_member_member_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team_member',
            name='cost_per_year',
        ),
    ]
