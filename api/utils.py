import easyocr
import re

reader = easyocr.Reader(['en'])

def extract_certificate_data(image_path):
    result = reader.readtext(image_path, detail=0)
    text = " ".join(result)
    name_match = re.search(r'This certificate is awarded to (.+?) for', text)
    course_match = re.search(r'completing the course (.+?) with', text)
    final_score_match = re.search(r'consolidated score of (\d+)', text)
    assignment_score_match = re.search(r'Online Assignments (\d+\.\d+)/25', text)
    proctored_score_match = re.search(r'Proctored Exam (\d+\.\d+)/75', text)
    year_match = re.search(r'(Jan|Jul)-\w+ (\d{4})', text)
    weeks_match = re.search(r'\((\d+) week course\)', text)
    credit_match = re.search(r'No. of credits recommended: (\d+)', text)
    roll_no_match = re.search(r'Roll No: (\w+)', text)

    final_score = int(final_score_match.group(1)) if final_score_match else 0

    grade_num = calculate_numeric_grade(final_score)
    grade_letter = calculate_letter_grade(final_score)

    # Extract and format the course code
    if roll_no_match:
        roll_no = roll_no_match.group(1)
        course_code = f"NOC{roll_no[5:7]}-{roll_no[7:11]}"
    else:
        course_code = ''

    return {
        'Dept': '',
        'Study Year': '',
        'College Roll No': '',
        'Student Name': name_match.group(1).strip() if name_match else '',
        'Course Code': course_code,
        'Course Name': course_match.group(1).strip() if course_match else '',
        'Sem': '',
        'Year of passing': year_match.group(2) if year_match else '',
        'Score from Assignment(25)': assignment_score_match.group(1) if assignment_score_match else '',
        'Proctored Exam Score(75)': proctored_score_match.group(1) if proctored_score_match else '',
        'Final Exam Score(100)': final_score,
        'Eligible for modified pass': 'Yes',
        'Week': weeks_match.group(1) if weeks_match else '',
        'Course Type Credit Transfer/Value Added': credit_match.group(1) if credit_match else '',
        'Credits as per MRIIRS Policy': '',
        'Grade(numeric) as per MRIIRS': grade_num,
        'Grade(letter) as per MRIIRS': grade_letter,
        'Timeline': year_match.group(0) if year_match else '',
    }

def calculate_numeric_grade(score):
    if score >= 90:
        return 10
    elif score >= 80:
        return 9
    elif score >= 70:
        return 8
    elif score >= 60:
        return 7
    elif score >= 50:
        return 6
    else:
        return 0

def calculate_letter_grade(score):
    if score >= 90:
        return 'A+'
    elif score >= 80:
        return 'A'
    elif score >= 70:
        return 'B+'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    else:
        return 'F'
  