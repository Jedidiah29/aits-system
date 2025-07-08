from django.db import models

# Create your models here.

class Issue(models.Model):
    ISSUE_TYPES = [
        ('MARKS', 'Missing Marks'),
        ('REGISTRATION', 'Course Registration'),
        ('COURSEWORK', 'Coursework Feedback'),
        ('TIMETABLE', 'Timetable Conflict'),
        ('OTHER', 'Other'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPES)
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.student_id})"
