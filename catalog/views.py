from django.shortcuts import render
from .models import Student
from django.core.paginator import Paginator, InvalidPage
from django.views.generic.detail import DetailView
from django.views import generic


# Create your views here.

def student_list(request, page):
    if request.method == 'GET':
        students = Student.objects.all()
        paginator = Paginator(students, 5)
        try:
            students_page = paginator.page(page)
        except InvalidPage:
            students_page = paginator.page(1)
        data = {
            'students': students_page,
            'current_page': page
        }
        return render(request, 'students/student-list.html', data)


class StudentListView(generic.ListView):
    model = Student
    queryset = Student.objects.all()
    template_name = 'students/student-list.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['current_page'] = self.kwargs.get('page')
        return data


class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'
    queryset = Student.objects.all()
    template_name = 'students/student-detail.html'

