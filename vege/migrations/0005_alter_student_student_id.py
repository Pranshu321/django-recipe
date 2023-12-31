# Generated by Django 4.1.3 on 2023-10-22 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("vege", "0004_department_studentid_student"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="studentid",
                to="vege.studentid",
            ),
        ),
    ]
