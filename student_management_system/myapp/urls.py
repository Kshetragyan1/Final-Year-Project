from django.urls import path
from .views import (
    school_teacher_list,
    school_teacher_detail,
    create_school_teacher,
    school_teacher_update,
    school_teacher_delete,
    college_teacher_list,
    college_teacher_detail,
    create_college_teacher,
    college_teacher_update,
    college_teacher_delete,
    both_teacher_list,
    both_teacher_detail,
    create_both_teacher,
    both_teacher_update,
    both_teacher_delete,
    create_school_student,
    school_student_list,
    school_student_detail,
    school_student_update,
    school_student_delete,
    create_college_student,
    college_student_list,
    college_student_detail,
    college_student_update,
    college_student_delete,
    homepage,
)

urlpatterns = [
    path('', homepage, name='homepage'),

    path('school_teachers/', school_teacher_list, name='school_teacher_list'),
    path('school_teachers/<int:pk>/', school_teacher_detail, name='school_teacher_detail'),
    path('school_teachers/create/', create_school_teacher, name='create_school_teacher'),
    path('school_teachers/<int:pk>/update/', school_teacher_update, name='school_teacher_update'),
    path('school_teachers/<int:pk>/delete/', school_teacher_delete, name='school_teacher_delete'),

    path('college_teachers/', college_teacher_list, name='college_teacher_list'),
    path('college_teachers/<int:pk>/', college_teacher_detail, name='college_teacher_detail'),
    path('college_teachers/create/', create_college_teacher, name='create_college_teacher'),
    path('college_teachers/<int:pk>/update/', college_teacher_update, name='college_teacher_update'),
    path('college_teachers/<int:pk>/delete/', college_teacher_delete, name='college_teacher_delete'),

    path('both_teachers/', both_teacher_list, name='both_teacher_list'),
    path('both_teachers/<int:pk>/', both_teacher_detail, name='both_teacher_detail'),
    path('both_teachers/create/', create_both_teacher, name='create_both_teacher'),
    path('both_teachers/<int:pk>/update/', both_teacher_update, name='both_teacher_update'),
    path('both_teachers/<int:pk>/delete/', both_teacher_delete, name='both_teacher_delete'),

    path('create_school_student/', create_school_student, name='create_school_student'),
    path('school_student_list/', school_student_list, name='school_student_list'),
    path('school_student_detail/<int:pk>/', school_student_detail, name='school_student_detail'),
    path('update_school_student/<int:pk>/', school_student_update, name='school_student_update'),
    path('delete_school_student/<int:pk>/', school_student_delete, name='school_student_delete'),


    path('create_college_student/', create_college_student, name='create_college_student'),
    path('college_student_list/', college_student_list, name='college_student_list'),
    path('college_student_detail/<int:pk>/', college_student_detail, name='college_student_detail'),
    path('update_college_student/<int:pk>/', college_student_update, name='college_student_update'),
    path('delete_college_student/<int:pk>/', college_student_delete, name='college_student_delete'),

]
