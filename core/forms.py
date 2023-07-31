from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import HTML, JS, PYTHON, Comment, Assignments

INPUT_STYLES = """
border-b w-[20rem] p-2 border-yellow-400
"""
INPUT_CLASSES = """
border-b w-[20rem] p-2 border-yellow-400 bg-gray-200
"""
HTML_CLASSES = """
border-b w-[20rem] p-2 border-red-400 bg-gray-200
"""
PYTHON_CLASSES = """
border-b w-[20rem] p-2 border-blue-400 bg-gray-200
"""
CHANGEPASSWORDFORM_CLASSES = """
border-b w-[20rem] p-2 border-yellow-400 text-yellow-500 bg-gray-300
"""


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_STYLES,
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': INPUT_STYLES,
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_STYLES,
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_STYLES,
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_STYLES,
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_STYLES,
    }))


class htmlForm(forms.ModelForm):
    class Meta:
        model = HTML
        fields = ('title', 'video_link', 'notes',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': HTML_CLASSES
            }),
            'video_link': forms.URLInput(attrs={
                'class': HTML_CLASSES
            }),
            'notes': forms.FileInput(attrs={
                'class': HTML_CLASSES
            }),
        }


class jsForm(forms.ModelForm):
    class Meta:
        model = JS
        fields = ('title', 'video_link', 'notes',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'video_link': forms.URLInput(attrs={
                'class': INPUT_CLASSES
            }),
            'notes': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }


class pythonForm(forms.ModelForm):
    class Meta:
        model = PYTHON
        fields = ('title', 'video_link', 'notes',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': PYTHON_CLASSES
            }),
            'video_link': forms.URLInput(attrs={
                'class': PYTHON_CLASSES
            }),
            'notes': forms.FileInput(attrs={
                'class': PYTHON_CLASSES
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('username', 'body',)
        widgets = {
            "username": forms.TextInput(attrs={
                'class': INPUT_STYLES
            }),
            "body": forms.Textarea(attrs={
                'class': 'w-[20rem] shadow-xl rounded-xl h-[5rem] py-2 px-2',
                'placeholder': 'Say something'
            })
        }


class AssignmentsForm(forms.ModelForm):
    class Meta:
        model = Assignments
        fields = ('username', 'courses', 'assignments',)
        widgets = {
            'username': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'courses': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'assignments': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': CHANGEPASSWORDFORM_CLASSES,
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': CHANGEPASSWORDFORM_CLASSES,
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': CHANGEPASSWORDFORM_CLASSES,
    }))
