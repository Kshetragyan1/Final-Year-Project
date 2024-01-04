from django import forms
from .models import SchoolTeacher, CollegeTeacher, BothTeacher
from .models import SchoolStudent, CollegeStudent

class SchoolTeacherForm(forms.ModelForm):
    class Meta:
        model = SchoolTeacher
        fields = [
            'school_teacher_id',
            'full_name',
            'education_degree',
            'address',
            'email',
            'mobile_number',
        ]


class CollegeTeacherForm(forms.ModelForm):
    class Meta:
        model = CollegeTeacher
        fields = [
            'college_teacher_id',
            'full_name',
            'education_degree',
            'address',
            'email',
            'mobile_number',
        ]

class BothTeacherForm(forms.ModelForm):
    class Meta:
        model = BothTeacher
        fields = [
            'both_teacher_id',
            'full_name',
            'education_degree',
            'address',
            'email',
            'mobile_number',
        ]

class SchoolStudentForm(forms.ModelForm):
    class Meta:
        model = SchoolStudent
        fields = [
            'school_student_roll_number',
            'school_student_registration_number',
            'full_name',
            'father_name',
            'address',
            'email',
            'mobile_number',
        ]


class CollegeStudentForm(forms.ModelForm):
    class Meta:
        model = CollegeStudent
        fields = [
            'college_student_roll_number',
            'college_student_registration_number',
            'full_name',
            'father_name',
            'address',
            'email',
            'mobile_number',
        ]
