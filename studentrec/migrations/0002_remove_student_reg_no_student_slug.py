# Generated by Django 4.0.6 on 2022-09-14 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentrec', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='reg_no',
        ),
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.CharField(default='FPI-COM-001', max_length=15, unique=True),
            preserve_default=False,
        ),
    ]
