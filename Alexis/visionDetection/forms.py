from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class NewUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ('name', 'country', 'phone_no', 'email', 'password',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()




class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('name', 'email', 'country', 'phone_no',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('name', 'email', 'country', 'phone_no',)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('name','country','phone_no','email')
