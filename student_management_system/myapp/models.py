from django.db import models

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    education_degree = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)

    class Meta:
        abstract = True

class SchoolTeacher(Teacher):
    school_teacher_id = models.CharField(max_length=20, unique=True)

class CollegeTeacher(Teacher):
    college_teacher_id = models.CharField(max_length=20, unique=True)

class BothTeacher(Teacher):
    both_teacher_id = models.CharField(max_length=20, unique=True)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    education_degree = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)

    class Meta:
        abstract = True

class SchoolStudent(Student):
    school_student_roll_number = models.CharField(max_length=20, unique=True)
    school_student_registration_number = models.CharField(max_length=20, unique=True)

class CollegeStudent(Student):
    college_student_roll_number = models.CharField(max_length=20, unique=True)
    college_student_registration_number = models.CharField(max_length=20, unique=True)

