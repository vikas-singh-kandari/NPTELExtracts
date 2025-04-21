from django.db import models
from django.contrib.auth.models import User

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dept = models.CharField(max_length=100, null=True)
    study_year = models.CharField(max_length=100, null=True)
    college_roll_no = models.CharField(max_length=100, null=True)
    student_name = models.CharField(max_length=200, null=True)
    course_code = models.CharField(max_length=100, null=True)
    course_name = models.CharField(max_length=200, null=True)
    sem = models.CharField(max_length=100, null=True)
    year_of_passing = models.CharField(max_length=100, null=True)
    assignment_score = models.FloatField(null=True)
    proctored_exam_score = models.FloatField(null=True)
    final_exam_score = models.FloatField(null=True)
    eligible_for_modified_pass = models.CharField(max_length=100, null=True)
    week = models.CharField(max_length=100,null=True)
    credit_transfer = models.CharField(max_length=100, null=True)
    credits_mriirs = models.CharField(max_length=100, null=True)
    grade_numeric = models.CharField(max_length=100, null=True)
    grade_letter = models.CharField(max_length=100, null=True)
    timeline = models.CharField(max_length=100, null=True)
    image_url = models.URLField(null=True)

    def __str__(self):
        return self.student_name
