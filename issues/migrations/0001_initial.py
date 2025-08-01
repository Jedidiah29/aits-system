# Generated by Django 5.2.4 on 2025-07-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Issue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "issue_type",
                    models.CharField(
                        choices=[
                            ("MARKS", "Missing Marks"),
                            ("REGISTRATION", "Course Registration"),
                            ("COURSEWORK", "Coursework Feedback"),
                            ("TIMETABLE", "Timetable Conflict"),
                            ("OTHER", "Other"),
                        ],
                        max_length=20,
                    ),
                ),
                ("student_name", models.CharField(max_length=100)),
                ("student_id", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_resolved", models.BooleanField(default=False)),
            ],
        ),
    ]
