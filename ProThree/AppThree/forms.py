from django.core import validators
from .models import VisitorList, UserProfileInfo
from django import forms
from django.contrib.auth.models import User


class NewUserForm(forms.ModelForm):
    # class Meta(): with brackets or without, it's same thing
    class Meta:
        model = VisitorList
        fields = "__all__"

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


# # def check_z(value):
# #     if value[0].lower() != 'z':
# #         raise forms.ValidationError("Name needs to start with z")
#
# class FormName(forms.Form):
#     # name = forms.CharField(validators=[check_z])
#     name = forms.CharField()
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='Enter your email again: ')
#     text = forms.CharField(widget=forms.Textarea)
#     # botcatcher = forms.CharField(required=False,
#     #                             widget=forms.HiddenInput,
#     #                             validators=[validators.MaxLengthValidator(0)])
#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         vmail = all_clean_data['verify_email']
#
#         if email != vmail:
#             raise forms.ValidationError("Make sure emails match")
#
#
#
# # We don't need to write such function for form validation, because django has inbuilt validators
#     # def clean_botcatcher(self):
#     #     botcatcher = self.cleaned_data['botcatcher']
#     #     if len(botcatcher) > 0:
#     #         raise forms.ValidationError('Gotcha Bot!')
#     #     return botcatcher
