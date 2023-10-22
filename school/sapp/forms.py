from django import forms

from .models import Department, Course


class LoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)




class DepartmentCourseForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.none())
class UserProfileForm(forms.Form):
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female'), ('other', 'Other')]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
