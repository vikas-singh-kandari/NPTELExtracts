from django.contrib import admin
from .models import Certificate

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
     list_display = [
        'user', 'dept', 'study_year', 'college_roll_no', 'student_name',
        'course_code', 'course_name', 'sem', 'year_of_passing',
        'assignment_score', 'proctored_exam_score', 'final_exam_score',
        'eligible_for_modified_pass', 'week', 'credit_transfer',
        'credits_mriirs', 'grade_numeric', 'grade_letter', 'timeline',
        'image_url']
 