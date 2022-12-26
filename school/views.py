from django.http import HttpResponse, request
from django.shortcuts import render

from school.models import Teacher, Student



from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    object_list = Student.objects.all()
    for student in object_list:
        student.teachers.all = student.teachers.all()
    template = 'school/students_list.html'
    context = {
        'header_students': 'Список учеников школы',
        'header_teachers': 'Список учителей студентов',
        'object_list': object_list,
        # 'student': students
    }
#     # используйте этот параметр для упорядочивания результатов
#     # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
#     # ordering = 'group'
#
    return render(request, template, context)

# students = Student.objects.all()
# for student in students:
#     print(student.name)
#     for teacher in student.teachers.all():
#     # teacher = student.teachers.all()
#     # print(student.name)
#         print(teacher.name, '->', teacher.subject)
    # print(teacher.name, '->', teacher.subject)



