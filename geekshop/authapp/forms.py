from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from authapp.models import User, UserProfile
import hashlib
import random


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Введите имя пользователя"
        self.fields["password"].widget.attrs["placeholder"] = "Введите пароль"
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control py-4"


class UserRegisterForm(UserCreationForm ):

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "last_name", "first_name", "email")

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Введите имя пользователя"
        self.fields["password1"].widget.attrs["placeholder"] = "Введите пароль"
        self.fields["password2"].widget.attrs["placeholder"] = "Повторите пароль"
        self.fields["last_name"].widget.attrs["placeholder"] = "Введите фамилию"
        self.fields["first_name"].widget.attrs["placeholder"] = "Введите имя"
        self.fields["email"].widget.attrs["placeholder"] = "Введите email"
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control py-4"

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode("utf-8")).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode("utf-8")).hexdigest()
        user.save()
        return user



class UserProfileForm(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    age = forms.IntegerField(widget=forms.NumberInput(), required=False)

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email", "image", "age")

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["readonly"] = True
        self.fields["email"].widget.attrs["readonly"] = True
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control py-4"

        self.fields["image"].widget.attrs["class"] = "custom-file-input"


class UserProfileEditForm(UserChangeForm):

    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super(UserProfileEditForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name != "gender":
                field.widget.attrs["class"] = "form-control py-4"
            else:
                field.widget.attrs["class"] = "form-control"
