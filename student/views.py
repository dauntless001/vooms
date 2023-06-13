from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View
from home.models import Student, Document
from student.forms import StudentForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages

# Create your views here.
class StudentsView(LoginRequiredMixin, ListView):
    context_object_name = 'students'
    template_name = 'student/students.html'
    paginate_by = 25

    def get_queryset(self):
        verified = self.request.GET.get('verified', True)
        return Student.objects.filter(published=verified)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['no_of_entries'] = Student.objects.count()
        return context


class StudentDetail(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'student/detail.html'
    context_object_name = 'student'

class CreateStudent(LoginRequiredMixin, TemplateView):
    template_name = 'student/create-student.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST, request.FILES)
        document_name = request.POST.getlist('document-name', None)
        document_file = request.FILES.getlist('document-file', None)
        if form.is_valid():
            if document_name and document_file:
                student = form.save(commit=False)
                student.published = True
                student.save()
                index = 0
                for a in document_name:
                    Document.objects.create(
                        name = a, document=document_file[index],
                        profile=student
                    )
                    index+=1
                messages.success(request, "Student profile added successfully")
                return HttpResponseRedirect(reverse_lazy("student:students"))
        return render(request, self.template_name, {'form':form})


class UpdateStudent(LoginRequiredMixin, TemplateView):
    template_name = 'student/edit-student.html'

    def get_student(self):
        return get_object_or_404(Student, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = self.get_student()
        context['form'] = StudentForm(instance=self.get_student())
        return context
    
    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST, request.FILES, instance=self.get_student())
        document_name = request.POST.getlist('document-name', None)
        document_file = request.FILES.getlist('document-file', None)
        if form.is_valid():
            form.save()
            if document_name and document_file:
                index = 0
                for a in document_name:
                    Document.objects.create(
                        name = a, document=document_file[index],
                        profile=self.get_student()
                    )
                    index+=1
            messages.success(request, f"{str(self.get_student())}'s profile updated successfully")
            return HttpResponseRedirect(reverse_lazy("student:students"))
        return render(request, self.template_name, {'form':form, 'student' : self.get_student()})


class DeleteStudent(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        student = get_object_or_404(Student, slug=self.kwargs['slug'])
        if student:
            student.delete()
            messages.success(request, "Student profile deleted successfully")
            return HttpResponseRedirect(reverse_lazy("student:students"))
        
        messages.error(request, "Failed to delete student profile")
        return HttpResponseRedirect(reverse_lazy("student:students"))


class DeleteDocument(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        document = get_object_or_404(Document, slug=self.kwargs['doc_slug'])
        if document:
            document.delete()
            messages.success(request, "Document deleted successfully")
        return HttpResponseRedirect(reverse_lazy("student:student-detail", kwargs={'slug' : self.kwargs['slug']}))


class VerifyStudent(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        student = get_object_or_404(Student, slug=self.kwargs['slug'])
        if student:
            student.published = True
            student.save()
            messages.success(request, "Student profile verified successfully")
            return HttpResponseRedirect(reverse_lazy("student:students"))
        
        messages.error(request, "Failed to verify student")
        return HttpResponseRedirect(reverse_lazy("student:student-detail", kwargs={'slug' : self.kwargs['slug']}))