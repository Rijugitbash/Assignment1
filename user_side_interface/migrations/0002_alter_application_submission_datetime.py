# Generated by Django 4.2.4 on 2023-08-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_side_interface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='submission_datetime',
            field=models.CharField(max_length=100),
        ),
    ]
