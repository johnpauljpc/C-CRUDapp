# Generated by Django 4.0.6 on 2022-09-14 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentrec', '0002_remove_student_reg_no_student_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='slug',
            new_name='reg_no',
        ),
    ]
