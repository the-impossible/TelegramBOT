# Generated by Django 4.1.6 on 2023-02-13 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Nacosbot_API", "0002_course_semester_title_material_lecturer_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="semester",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="Nacosbot_API.semester",
            ),
            preserve_default=False,
        ),
    ]