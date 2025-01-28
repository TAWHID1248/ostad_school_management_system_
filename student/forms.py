from django.forms import ModelForm

from . import models 

class StudentForm(ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__'
        labels = {
            'name': 'Student Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'course': 'Course Name',
        }