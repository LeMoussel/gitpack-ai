# Generated by Django 5.1 on 2024-10-03 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_organization_third_party_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='is_enabled',
            field=models.BooleanField(default=True),
        ),
    ]
