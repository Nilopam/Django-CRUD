# Generated by Django 4.1.1 on 2022-09-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile_no',
            field=models.CharField(max_length=12),
        ),
    ]
