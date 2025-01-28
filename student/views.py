from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import models 
from .  import forms

# class based views
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
from django.contrib import messages #import messages

class StudentListViews(ListView):
    model = models.Student
    context_object_name = 'students'
    template_name = 'student/student_list.html'
    ordering = ['-id']

class AddStudentView(CreateView):
    form_class = forms.StudentForm
    context_object_name = 'form'
    success_url = reverse_lazy('home')
    template_name = 'student/add_student_form.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        messages.success(self.request, "Student add successfully.")
        return super().form_valid(form)
    
class StudentUpdateViews(UpdateView):
    pk_url_kwarg = 'id'
    model = models.Student
    form_class = forms.StudentForm
    context_object_name = 'form'
    success_url = reverse_lazy('home')
    template_name = 'student/update_student_form.html'


    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        messages.warning(self.request, "Student updated successfully.")
        return super().form_valid(form)



class StudentDeleteViews(DeleteView):
    pk_url_kwarg = 'id'
    model = models.Student
    template_name = 'student/delete_student.html'
    success_url = reverse_lazy('home')
    
    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        messages.error(self.request, "Student deleted.")
        return super().delete(request, *args, **kwargs)