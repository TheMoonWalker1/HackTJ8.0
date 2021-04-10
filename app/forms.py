from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))


class CarForm(forms.Form):
    vin = forms.CharField(label='VIN', required=True, max_length=17)


