# Generated by Django 4.2.1 on 2023-05-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_remove_student_name_student_gpa_student_birthdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
