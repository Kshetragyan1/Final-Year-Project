from django.shortcuts import render, get_object_or_404, redirect
from .models import SchoolTeacher, CollegeTeacher, BothTeacher
from .forms import SchoolTeacherForm, CollegeTeacherForm, BothTeacherForm
from .models import SchoolStudent, CollegeStudent
from .forms import SchoolStudentForm, CollegeStudentForm

def homepage(request):
    school_teachers = SchoolTeacher.objects.all()
    college_teachers = CollegeTeacher.objects.all()
    both_teachers = BothTeacher.objects.all()
    school_students=SchoolStudent.objects.all()
    college_students=CollegeStudent.objects.all()



    context = {
        'school_teachers': school_teachers,
        'college_teachers': college_teachers,
        'both_teachers': both_teachers,
        'school_students':school_students,
        'college_students':college_students,

    }

    return render(request, 'myapp/homepage.html', context)

def create_school_teacher(request):
    if request.method == 'POST':
        form = SchoolTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school_teacher_list')
    else:
        form = SchoolTeacherForm()
    return render(request, 'myapp/create_school_teacher.html', {'form': form})

def school_teacher_list(request):
    teachers = SchoolTeacher.objects.all()
    return render(request, 'myapp/school_teacher_list.html', {'teachers': teachers})

def school_teacher_detail(request, pk):
    teacher = get_object_or_404(SchoolTeacher, pk=pk)
    return render(request, 'myapp/school_teacher_detail.html', {'teacher': teacher})

def school_teacher_update(request, pk):
    teacher = get_object_or_404(SchoolTeacher, pk=pk)

    if request.method == 'POST':
        form = SchoolTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('school_teacher_detail', pk=pk)
    else:
        form = SchoolTeacherForm(instance=teacher)

    return render(request, 'myapp/school_teacher_update.html', {'form': form, 'teacher': teacher})


def school_teacher_delete(request, pk):
    teacher = get_object_or_404(SchoolTeacher, pk=pk)

    if request.method == 'POST':
        teacher.delete()
        return redirect('school_teacher_list')

    return render(request, 'myapp/school_teacher_delete.html', {'teacher': teacher})


def create_college_teacher(request):
    if request.method == 'POST':
        form = CollegeTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('college_teacher_list')
    else:
        form = CollegeTeacherForm()

    return render(request, 'myapp/create_college_teacher.html', {'form': form})

def college_teacher_list(request):
    teachers = CollegeTeacher.objects.all()
    return render(request, 'myapp/college_teacher_list.html', {'teachers': teachers})

def college_teacher_detail(request, pk):
    teacher = get_object_or_404(CollegeTeacher, pk=pk)
    return render(request, 'myapp/college_teacher_detail.html', {'teacher': teacher})


def college_teacher_update(request, pk):
    teacher = get_object_or_404(CollegeTeacher, pk=pk)

    if request.method == 'POST':
        form = CollegeTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('college_teacher_detail', pk=pk)
    else:
        form = CollegeTeacherForm(instance=teacher)

    return render(request, 'myapp/college_teacher_update.html', {'form': form, 'teacher': teacher})

def college_teacher_delete(request, pk):
    teacher = get_object_or_404(CollegeTeacher, pk=pk)

    if request.method == 'POST':
        teacher.delete()
        return redirect('college_teacher_list')

    return render(request, 'myapp/college_teacher_delete.html', {'teacher': teacher})


def create_both_teacher(request):
    if request.method == 'POST':
        form = BothTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('both_teacher_list')
    else:
        form = BothTeacherForm()

    return render(request, 'myapp/create_both_teacher.html', {'form': form})


def both_teacher_list(request):
    teachers = BothTeacher.objects.all()
    return render(request, 'myapp/both_teacher_list.html', {'teachers': teachers})

def both_teacher_detail(request, pk):
    teacher = get_object_or_404(BothTeacher, pk=pk)
    return render(request, 'myapp/both_teacher_detail.html', {'teacher': teacher})


def both_teacher_update(request, pk):
    teacher = get_object_or_404(BothTeacher, pk=pk)

    if request.method == 'POST':
        form = BothTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('both_teacher_detail', pk=pk)
    else:
        form = BothTeacherForm(instance=teacher)

    return render(request, 'myapp/both_teacher_update.html', {'form': form, 'teacher': teacher})

def both_teacher_delete(request, pk):
    teacher = get_object_or_404(BothTeacher, pk=pk)

    if request.method == 'POST':
        teacher.delete()
        return redirect('both_teacher_list')

    return render(request, 'myapp/both_teacher_delete.html', {'teacher': teacher})

def create_school_student(request):
    if request.method == 'POST':
        form = SchoolStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school_student_list')
    else:
        form = SchoolStudentForm()
    return render(request, 'myapp/create_school_student.html', {'form': form})

def school_student_list(request):
    students = SchoolStudent.objects.all()
    print(students)
    return render(request, 'myapp/school_student_list.html', {'students': students})

def school_student_detail(request,pk):
    student = get_object_or_404(SchoolStudent, pk=pk)
    return render(request, 'myapp/school_student_detail.html', {'student': student})

def school_student_update(request, pk):
    student = get_object_or_404(SchoolStudent, pk=pk)
    if request.method == 'POST':
        form = SchoolStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('school_student_list')
    else:
        form = SchoolStudentForm(instance=student)
    return render(request, 'myapp/school_student_update.html', {'form': form, 'student': student})

def school_student_delete(request, pk):
    student = get_object_or_404(SchoolStudent, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('school_student_list')
    return render(request, 'myapp/school_student_delete.html', {'student': student})


def create_college_student(request):
    if request.method == 'POST':
        form = CollegeStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('college_student_list')
    else:
        form = CollegeStudentForm()
    return render(request, 'myapp/create_college_student.html', {'form': form})

def college_student_list(request):
    students = CollegeStudent.objects.all()
    return render(request, 'myapp/college_student_list.html', {'students': students})

def college_student_detail(request, pk):
    student = get_object_or_404(CollegeStudent, pk=pk)
    return render(request, 'myapp/college_student_detail.html', {'student': student})

def college_student_update(request, pk):
    student = get_object_or_404(CollegeStudent, pk=pk)
    if request.method == 'POST':
        form = CollegeStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('college_student_list')
    else:
        form = CollegeStudentForm(instance=student)
    return render(request, 'myapp/college_student_update.html', {'form': form, 'student': student})

def college_student_delete(request, pk):
    student = get_object_or_404(CollegeStudent, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('college_student_list')
    return render(request, 'myapp/college_student_delete.html', {'student': student})


