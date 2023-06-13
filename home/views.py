from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from home.forms import UserForm
from student.forms import StudentForm
from django.urls import reverse_lazy
from django.contrib import messages
from home.models import Student, Document
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class AboutUs(TemplateView):
    template_name = 'about.html'

class ContactUs(TemplateView):
    template_name = 'contact.html'

class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.filter(published=True)[:5]
        context['student_count'] = Student.objects.all().count()
        context['verified_students'] = Student.objects.filter(published=True).count()
        context['unverified_students'] = Student.objects.filter(published=False).count()
        return context


class EditProfile(LoginRequiredMixin, TemplateView):
    template_name = 'edit-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserForm(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST, request.FILES,instance=self.request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return HttpResponseRedirect(reverse_lazy("home:edit-profile"))
        return render(request, self.template_name, {'form':form})


class CreateProfile(TemplateView):
    template_name = 'create-profile.html'

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
                student.save()
                index = 0
                for a in document_name:
                    Document.objects.create(
                        name = a, document=document_file[index],
                        profile=student
                    )
                    index+=1
                messages.success(request, "Profile sent successfully, wait while it is being reviewed")
                return HttpResponseRedirect(reverse_lazy("home:student-profile"))
        return render(request, self.template_name, {'form':form})

