from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя')
    email = forms.EmailField(label='Электронная почта', max_length=254)
    password1 = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Подтверждение пароля')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Пользователь с таким именем уже существует.')
        return username    

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('Пароли не совпадают.')

        if len(password1) < 8:
            raise ValidationError('Этот пароль слишком короткий. Он должен содержать как минимум 8 символов.')

        if password1.isdigit():
            raise ValidationError('Этот пароль полностью числовой.')

        return password2


class MyLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Ваш адрес электронной почты', max_length=254)

class MyPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=("Новый пароль"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )

    new_password2 = forms.CharField(
        label=("Подтверждение нового пароля"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", 'username']

