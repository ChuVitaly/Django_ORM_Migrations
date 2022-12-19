from django.http import HttpResponse, request
from django.shortcuts import render

from school.models import Teacher, Student



from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    object_list = Student.objects.all()
    template = 'school/students_list.html'
    # students = Student.object.filter(students=teacher).order_by('teachers')
    context = {
        'header_students': 'Список студентов',
        'header_teachers': 'Список учителей студентов',
        'object_list': object_list,
        # 'student': students
    }
#     # используйте этот параметр для упорядочивания результатов
#     # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
#     # ordering = 'group'
#
    return render(request, template, context)
