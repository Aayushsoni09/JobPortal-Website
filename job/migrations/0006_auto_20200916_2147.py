# Generated by Django 3.0.7 on 2020-09-16 16:17

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_remove_cand_details_regdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cand_details',
            name='contact',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]
