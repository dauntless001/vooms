from allauth.account.forms import LoginForm, SignupForm, ChangePasswordForm
from django.contrib.auth.forms import PasswordChangeForm
from django import forms

from voomsdb.utils.forms import CssForm
from home.models import User, Student, Document

class UserForm(CssForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'email' : forms.EmailInput(attrs={'readonly' : True})
        }


class CustomLoginForm(CssForm, LoginForm):
    pass


class PasswordUpdateForm(PasswordChangeForm, CssForm):
    class Meta:
        model = User
        fields = "__all__"


class CustomChangePasswordForm(ChangePasswordForm, CssForm):
    pass




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