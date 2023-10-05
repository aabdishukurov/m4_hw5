from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, 'Администратор'),
    (VIPClient, 'VIP Клиент'),
    (CLIENT, 'Клиент')
)

MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE, 'М'),
    (FEMALE, 'Ж')
)

class RegistraionNewForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'user_type',
            'gender'
        )

    def save(self, commit=True):
        user = super(RegistraionNewForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user