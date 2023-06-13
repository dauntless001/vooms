from django import forms
from voomsdb.utils.forms import CssForm
from home.models import User, Student, Document





class StudentForm(CssForm, forms.ModelForm):
    class Meta:
        model = Student
        exclude = [
            'created_at', 'updated_at', 'published'
        ]

        widgets = {
            "address" : forms.Textarea(attrs={'rows' : 3})
        }


class DocumentForm(CssForm, forms.ModelForm):
    class Meta:
        model = Document
        exclude = [
            'profile',
        ]